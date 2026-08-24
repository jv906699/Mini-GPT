import re
import streamlit as st
import numpy as np
from peft import PeftModel


# ============================================================
# Mini GPT
# TinyLlama 1.1B + LoRA + RAG + Multi-Agent Routing
# ============================================================


# ------------------------------------------------------------
# Load LLM
# ------------------------------------------------------------
@st.cache_resource
def load_llm():
    from transformers import (
        AutoTokenizer,
        AutoModelForCausalLM,
        pipeline
    )

    base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    tokenizer = AutoTokenizer.from_pretrained(
        base_model
    )

    model = AutoModelForCausalLM.from_pretrained(
        base_model
    )

    # Load your fine-tuned LoRA adapter
    model = PeftModel.from_pretrained(
        model,
        "jatin-verma-ai/intelliagent-model"
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=120,
        temperature=0.6,
        do_sample=False,
        repetition_penalty=1.2
    )

    return pipe


# ------------------------------------------------------------
# Load RAG Knowledge Base
# ------------------------------------------------------------
@st.cache_resource
def load_rag():
    from sentence_transformers import SentenceTransformer
    import faiss

    # Small demonstration knowledge base
    documents = [
        (
            "Artificial Intelligence (AI) is a field of computer "
            "science focused on building systems that can perform "
            "tasks that normally require human intelligence, such "
            "as reasoning, learning, perception, and language "
            "understanding."
        ),

        (
            "Machine learning is a branch of artificial intelligence "
            "in which computer systems learn patterns from data and "
            "use those patterns to make predictions or decisions."
        ),

        (
            "Gradient descent is an optimization algorithm commonly "
            "used to minimize a machine learning model's loss "
            "function by iteratively adjusting model parameters "
            "in the direction that reduces the loss."
        ),

        (
            "Overfitting occurs when a machine learning model learns "
            "the training data too closely, including noise or "
            "irrelevant patterns, and therefore performs poorly "
            "on previously unseen data."
        ),

        (
            "Neural networks are machine learning models composed "
            "of interconnected layers of artificial neurons. "
            "They can learn complex relationships in data and are "
            "widely used in computer vision, natural language "
            "processing, and other AI applications."
        ),

        (
            "Retrieval-Augmented Generation (RAG) is a technique "
            "that combines information retrieval with language "
            "model generation. A RAG system first retrieves relevant "
            "information from an external knowledge base and then "
            "provides that information to a language model as "
            "context for generating an answer."
        ),

        (
            "FAISS is a library for efficient similarity search "
            "and clustering of dense vectors. In this project, "
            "FAISS stores document embeddings and retrieves the "
            "documents whose vectors are most similar to a user's "
            "query embedding."
        ),

        (
            "Sentence Transformers are models used to convert "
            "sentences or documents into numerical vector "
            "embeddings. In this project, Sentence Transformers "
            "create embeddings for the RAG knowledge base and "
            "for user queries."
        ),

        (
            "LoRA, or Low-Rank Adaptation, is a parameter-efficient "
            "fine-tuning technique. Instead of updating all the "
            "parameters of a language model, LoRA trains a smaller "
            "set of additional parameters that can be loaded as "
            "an adapter."
        ),

        (
            "TinyLlama 1.1B is a lightweight language model with "
            "approximately 1.1 billion parameters. In this project, "
            "TinyLlama/TinyLlama-1.1B-Chat-v1.0 is used as the base "
            "language model together with a LoRA adapter."
        ),

        (
            "Multi-agent routing is an approach in which a user's "
            "query is analyzed and directed to a specialized "
            "agent or tool. In this project, queries are routed "
            "between a general LLM agent, a RAG agent, and a "
            "calculator agent."
        ),

        (
            "The Mini GPT project combines a fine-tuned TinyLlama "
            "language model, LoRA, Retrieval-Augmented Generation "
            "using Sentence Transformers and FAISS, a calculator "
            "tool, conversational memory, and Streamlit to provide "
            "a lightweight AI assistant."
        )
    ]

    # Embedding model
    embed_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    # Generate embeddings
    embeddings = embed_model.encode(
        documents,
        convert_to_numpy=True
    )

    embeddings = embeddings.astype(
        np.float32
    )

    # Create FAISS index
    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(
        embeddings
    )

    return (
        embed_model,
        index,
        documents
    )


# ------------------------------------------------------------
# Calculator Agent
# ------------------------------------------------------------
def calculator_tool(query):

    try:
        expression = query.lower().strip()

        # Remove common calculation phrases
        expression = re.sub(
            r"\b(calculate|compute)\b",
            "",
            expression
        ).strip()

        # Handle "what is 25 * 16"
        expression = re.sub(
            r"^what\s+is\s+",
            "",
            expression
        ).strip()

        # Only allow basic arithmetic
        if not re.fullmatch(
            r"[0-9+\-*/().\s]+",
            expression
        ):
            return (
                "⚠️ I can calculate basic arithmetic "
                "expressions only."
            )

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception:
        return "⚠️ Calculation error."


# ------------------------------------------------------------
# Query Router
# ------------------------------------------------------------
def route_query(query):

    q = query.lower().strip()

    # Detect actual arithmetic expressions
    arithmetic_pattern = (
        r"^\s*"
        r"(?:calculate|compute|what\s+is)?"
        r"\s*"
        r"[0-9]+(?:\s*[+\-*/]\s*[0-9().]+)+"
        r"\s*$"
    )

    if re.fullmatch(
        arithmetic_pattern,
        q
    ):
        return "calculator"

    # Questions that benefit from the RAG knowledge base
    rag_keywords = [
        "what is",
        "what are",
        "explain",
        "define",
        "why",
        "how does",
        "how do",
        "tell me about"
    ]

    if any(
        keyword in q
        for keyword in rag_keywords
    ):
        return "rag"

    # Everything else goes to the general LLM
    return "llm"


# ------------------------------------------------------------
# Retrieve relevant documents
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
        np.float32
    )

    distances, indices = index.search(
        query_embedding,
        2
    )

    results = []

    for distance, index_id in zip(
        distances[0],
        indices[0]
    ):
        results.append(
            documents[index_id]
        )

    return "\n\n".join(results)


# ------------------------------------------------------------
# Clean LLM Output
# ------------------------------------------------------------
def clean_output(text):

    text = text.strip()

    # Remove our prompt's answer marker if generated
    if "Answer:" in text:
        text = text.split(
            "Answer:",
            1
        )[-1].strip()

    unwanted_phrases = [
        "Context:",
        "You are a helpful AI assistant"
    ]

    for phrase in unwanted_phrases:
        text = text.replace(
            phrase,
            ""
        )

    # Stop accidental conversation continuation
    stop_markers = [
        "\nUser:",
        "\nuser:",
        "\nAssistant:",
        "\nassistant:"
    ]

    for marker in stop_markers:
        if marker in text:
            text = text.split(
                marker,
                1
            )[0].strip()

    return text.strip()


# ------------------------------------------------------------
# Generate LLM Response
# ------------------------------------------------------------
def generate_answer(
    prompt,
    pipe
):

    result = pipe(
        prompt
    )

    generated_text = result[0][
        "generated_text"
    ]

    return clean_output(
        generated_text
    )


# ------------------------------------------------------------
# Load Models
# ------------------------------------------------------------
pipe = load_llm()

(
    embed_model,
    index,
    documents
) = load_rag()


# ------------------------------------------------------------
# Chat Memory
# ------------------------------------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = []


# ------------------------------------------------------------
# UI
# ------------------------------------------------------------
st.title(
    "🤖 Mini GPT"
)

st.caption(
    "TinyLlama 1.1B + LoRA + RAG + Multi-Agent Routing"
)


# ------------------------------------------------------------
# Display Chat History
# ------------------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.write(
            message["content"]
        )


# ------------------------------------------------------------
# Chat Input
# ------------------------------------------------------------
query = st.chat_input(
    "Ask something..."
)


if query:

    # --------------------------------------------------------
    # Display user's message immediately
    # --------------------------------------------------------
    with st.chat_message(
        "user"
    ):
        st.write(
            query
        )

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # --------------------------------------------------------
    # Conversation Memory
    # --------------------------------------------------------
    conversation = ""

    for message in (
        st.session_state.messages[-5:]
    ):
        conversation += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    # --------------------------------------------------------
    # Route Query
    # --------------------------------------------------------
    agent = route_query(
        query
    )


    # ========================================================
    # Calculator Agent
    # ========================================================
    if agent == "calculator":

        answer = calculator_tool(
            query
        )


    # ========================================================
    # RAG Agent
    # ========================================================
    elif agent == "rag":

        context = retrieve(
            query,
            embed_model,
            index,
            documents
        )

        prompt = f"""
You are a helpful AI assistant.

Conversation:
{conversation}

Use the following retrieved context to answer
the current question.

Retrieved context:
{context}

Important instructions:
- Answer the current question directly.
- Use the retrieved context when it contains the answer.
- Do not invent definitions or facts.
- Do not create a fictional conversation.
- Do not claim to have access to the internet.
- If the retrieved context does not contain enough
  information, say that the information is not
  available in the current knowledge base.

Question:
{query}

Answer:
"""

        answer = generate_answer(
            prompt,
            pipe
        )


    # ========================================================
    # General LLM Agent
    # ========================================================
    else:

        prompt = f"""
You are Mini GPT, a helpful AI assistant.

Conversation:
{conversation}

Answer the current user's question clearly
and concisely.

Do not invent previous user messages.
Do not create fictional conversations.
Do not claim to have internet access or external
tools unless they are explicitly provided.

Question:
{query}

Answer:
"""

        answer = generate_answer(
            prompt,
            pipe
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
    # Display Assistant Response
    # --------------------------------------------------------
    with st.chat_message(
        "assistant"
    ):
        st.write(
            answer
        )
