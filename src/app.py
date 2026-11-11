"""
From midterm-project, run:
streamlit run src/app.py
"""
from __future__ import annotations

import sys
import pathlib

import chromadb
import streamlit as st


# Resolve every project file from this source file, not the terminal's cwd.
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
sys.path[:0] = [str(PROJECT_ROOT), str(DATA_DIR)]

from coursekit import EMBED_MODEL, MissingKey, converse, embed  # noqa: E402
from hw1_corpus import FAMINE as DOCUMENTS

# three prompting techniques: role prompting, context grounding, and format constraints
SYSTEM_PROMPT = (
    "You are a food-security explainer helping students compare interventions. "
    "Use ONLY the retrieved context for factual answers. "
    "If it does not contain the answer, say the corpus does not provide enough information. "
    "Do not use outside knowledge or invent region-specific advice. "
    "Use conversation history to understand follow-up questions and remember what the user asked, "
    "but do not treat previous answers as factual evidence. "
    "For factual answers, use three short sections: Answer, Evidence, and Limitations. "
    "In Evidence, identify supporting context paragraph numbers. "
    "For questions about the conversation itself, answer directly from the conversation history. "
)
MODEL = "gpt-oss"
TOP_K = 5
TEMPERATURE = 0.2
COLLECTION = "b490_midterm"
USE_REFLECTION = True



# Build once and reuse the saved vectors on later runs
@st.cache_resource(show_spinner="Embedding the corpus...")
def build_index(docs: tuple[str, ...]):
    """Embed the corpus only if the saved collection is empty."""
    store = chromadb.PersistentClient(path=str(DATA_DIR / "chroma"))
    coll = store.get_or_create_collection(COLLECTION, embedding_function=None)
    if coll.count() == 0:
        vectors = embed(list(docs))
        coll.add(
            ids=[str(i) for i in range(len(docs))],
            embeddings=vectors,
            documents=list(docs),
        )
    return coll


def retrieve(coll, question: str, k: int = TOP_K) -> list[str]:
    """Embed the question and find the nearest documents."""
    hits = coll.query(query_embeddings=embed(question), n_results=min(k, coll.count()))
    return hits["documents"][0] if hits.get("documents") else []


def answer(question: str, context: list[str], history: list[dict]) -> str:
    """Use conversation history, retrieved context, and one reflection pass."""
    joined = "\n".join(f"[{i + 1}] {c}" for i, c in enumerate(context))
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": f"Context:\n{joined}\n\nQuestion: {question}"})
    reply = converse(messages, model=MODEL, temperature=TEMPERATURE)

    # Reflection loop when specified. Rechecks output for missing evidence and unsupported statements
    for _ in range(1 if USE_REFLECTION else 0):
        messages.append({"role": "assistant", "content": reply})
        messages.append({
            "role": "user",
            "content": (
                "Review your draft against the supplied context and the original question. "
                "Correct unsupported claims and incorrect paragraph references. "
                "If evidence is missing, admit the fault clearly instead of guessing. "
                "If the question is about our conversation, check the conversation history. "
                "Return only the final answer, keeping the required format."
            ),
        })
        reply = converse(messages, model=MODEL, temperature=TEMPERATURE)
    return reply


def main():
    st.set_page_config(page_title="Famine Query Chat", page_icon="[]")
    st.title("Famine Query Chat")
    st.caption(f"Retrieval over {len(DOCUMENTS)} documents, answered by {MODEL} on NRP")


    # Chatbot interface: messaging, retrieval, and memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])


    if prompt := st.chat_input("Ask about food security or compare interventions..."):
        history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                collection = build_index(tuple(DOCUMENTS))
                context = retrieve(collection, prompt)
                with st.expander(f"Retrieved {len(context)} document(s)"):
                    for i, c in enumerate(context):
                        st.write(f"[{i + 1}] {c}")
                reply = answer(prompt, context, history)
            except MissingKey as exc:
                st.error(str(exc))
            except Exception as exc:
                st.error(f"Request failed: {exc}")
                st.info(f"Check that {MODEL} and {EMBED_MODEL} are reachable and your key is valid.")
            else:
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
