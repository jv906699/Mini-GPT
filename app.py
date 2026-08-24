import streamlit as st
import numpy as np
import torch
from peft import PeftModel


# ============================================================
# MINI GPT
# TinyLlama 1.1B + LoRA + RAG + Multi-Agent Routing
# ============================================================


# ------------------------------------------------------------
# Load Fine-Tuned LLM
# ------------------------------------------------------------
@st.cache_resource(show_spinner="Loading Mini GPT model...")
def load_llm():

    from transformers import (
        AutoTokenizer,
        AutoModelForCausalLM,
        pipeline
    )

    base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    adapter_model = "jatin-verma-ai/intelliagent-model"

    tokenizer = AutoTokenizer.from_pretrained(base_model)

    model = AutoModelForCausalLM.from_pretrained(
        base_model
    )

    # Load your trained LoRA adapter
    model = PeftModel.from_pretrained(
        model,
        adapter_model
    )

    # Inference mode
    model.eval()

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,

        # Faster generation
        max_new_tokens=60,

        # Deterministic generation
        do_sample=False,

        # Prevent unnecessary repetition
        repetition_penalty=1.1,

        # Don't return the original prompt
        return_full_text=False
    )

    return pipe


# ------------------------------------------------------------
# Load RAG System
# ------------------------------------------------------------
@st.cache_resource(show_spinner="Loading RAG system...")
def load_rag():

    from sentence_transformers import SentenceTransformer
    import faiss

    documents = [
        "Gradient descent is an optimization algorithm used to minimize loss.",
        "Overfitting occurs when a model learns training data too well and fails on new data.",
        "Neural networks are inspired by the human brain and consist of layers of neurons.",
        "Machine learning is a method where computers learn patterns from data."
    ]

    # Embedding model
    embed_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    embeddings = embed_model.encode(
        documents,
        convert_to_numpy=True
    )

    # FAISS vector index
    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(
        embeddings.astype("float32")
    )

    return embed_model, index, documents


# ------------------------------------------------------------
# Calculator Agent
# ------------------------------------------------------------
def calculator_tool(query):

    try:
        # Extract a simple mathematical expression
        expression = query.lower()

        expression = (
            expression
            .replace("calculate", "")
            .replace("what is", "")
            .replace("=", "")
            .strip()
        )

        # Basic calculator
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception:
        return "⚠️ I couldn't calculate that expression."


# ------------------------------------------------------------
# Query Router
# ------------------------------------------------------------
def route_query(query):

    q = query.lower().strip()

    # Calculator
    math_words = [
        "calculate",
        "plus",
        "minus",
        "multiply",
        "divide"
    ]

    math_symbols = ["+", "*", "/"]

    if (
        any(word in q for word in math_words)
        or any(symbol in q for symbol in math_symbols)
    ):
        return "calculator"

    # RAG
    rag_words = [
        "what is",
        "what are",
        "explain",
        "define",
        "why",
        "how does",
        "how do"
    ]

    if any(word in q for word in rag_words):
        return "rag"

    # General LLM
    return "llm"


# ------------------------------------------------------------
# RAG Retrieval
# ------------------------------------------------------------
def retrieve(
    query,
    embed_model,
    index,
    documents
):

    query_embedding = embed_model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = query_embedding.astype(
        "float32"
    )

    _, indices = index.search(
        query_embedding,
        1
    )

    return documents[indices[0][0]]


# ------------------------------------------------------------
# Clean Model Output
# ------------------------------------------------------------
def clean_output(text):

    unwanted = [
        "Context:",
        "You are a helpful AI assistant",
        "Answer:",
        "Question:",
        "Use the context only if useful"
    ]

    for item in unwanted:
        text = text.replace(item, "")

    return text.strip()


# ------------------------------------------------------------
# Load Resources
# ------------------------------------------------------------
pipe = load_llm()

embed_model, index, documents = load_rag()


# ------------------------------------------------------------
# Chat Memory
# ------------------------------------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = []


# ------------------------------------------------------------
# UI
# ------------------------------------------------------------
st.title("🤖 Mini GPT")

st.caption(
    "TinyLlama 1.1B + LoRA + RAG + Multi-Agent Routing"
)


# ------------------------------------------------------------
# Display Previous Chat History
# ------------------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ------------------------------------------------------------
# Chat Input
# ------------------------------------------------------------
query = st.chat_input("Ask something...")


# ------------------------------------------------------------
# Process New Query
# ------------------------------------------------------------
if query:

    # Show the user's question immediately
    with st.chat_message("user"):
        st.write(query)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )


    # --------------------------------------------------------
    # Keep recent conversation
    # --------------------------------------------------------
    recent_messages = st.session_state.messages[-2:]

    conversation = ""

    for message in recent_messages:

        conversation += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )


    # --------------------------------------------------------
    # Route Query
    # --------------------------------------------------------
    agent = route_query(query)


    # --------------------------------------------------------
    # Calculator Agent
    # --------------------------------------------------------
    if agent == "calculator":

        answer = calculator_tool(query)


    # --------------------------------------------------------
    # RAG Agent
    # --------------------------------------------------------
    elif agent == "rag":

        context = retrieve(
            query,
            embed_model,
            index,
            documents
        )

        prompt = f"""Answer the question briefly.

Context:
{context}

Question:
{query}

Answer:"""

        with st.spinner("Thinking..."):

            with torch.inference_mode():

                result = pipe(prompt)

        answer = clean_output(
            result[0]["generated_text"]
        )


    # --------------------------------------------------------
    # General LLM Agent
    # --------------------------------------------------------
    else:

        prompt = f"""Answer the user briefly and clearly.

Conversation:
{conversation}

User:
{query}

Assistant:"""

        with st.spinner("Thinking..."):

            with torch.inference_mode():

                result = pipe(prompt)

        answer = clean_output(
            result[0]["generated_text"]
        )


    # --------------------------------------------------------
    # Save Assistant Response
    # --------------------------------------------------------
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    # --------------------------------------------------------
    # Display Assistant Response Immediately
    # --------------------------------------------------------
    with st.chat_message("assistant"):

        st.write(answer)
