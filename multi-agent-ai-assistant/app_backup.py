import streamlit as st
import numpy as np
from peft import PeftModel

# ---------------------------
# 🔹 Load LLM (cached)
# ---------------------------
@st.cache_resource
def load_llm():
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

    base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model)
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


# ---------------------------
# 🔹 Load RAG (cached)
# ---------------------------
@st.cache_resource
def load_rag():
    from sentence_transformers import SentenceTransformer
    import faiss

    documents = [
        "Gradient descent is an optimization algorithm used to minimize loss.",
        "Overfitting occurs when a model learns training data too well and fails on new data.",
        "Neural networks are inspired by the human brain and consist of layers of neurons.",
        "Machine learning is a method where computers learn patterns from data."
    ]

    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embed_model.encode(documents)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return embed_model, index, documents


# ---------------------------
# 🔹 Tools (Agents)
# ---------------------------
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "⚠️ Calculation error"


def route_query(query):
    q = query.lower()

    if any(x in q for x in ["+", "-", "*", "/", "calculate"]):
        return "calculator"
    elif any(x in q for x in ["what", "explain", "define", "why", "how"]):
        return "rag"
    else:
        return "llm"


# ---------------------------
# 🔹 Retrieve function
# ---------------------------
def retrieve(query, embed_model, index, documents):
    q = embed_model.encode([query])
    _, idx = index.search(np.array(q), 2)
    return "\n".join([documents[i] for i in idx[0]])


# ---------------------------
# 🔹 Clean output
# ---------------------------
def clean_output(text):
    if "Answer:" in text:
        text = text.split("Answer:")[-1]

    unwanted = ["Context:", "You are a helpful AI assistant"]
    for u in unwanted:
        text = text.replace(u, "")

    return text.strip()


# ---------------------------
# 🔹 Load models
# ---------------------------
pipe = load_llm()
embed_model, index, documents = load_rag()


# ---------------------------
# 🔹 Chat Memory
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------
# 🔹 UI
# ---------------------------
st.title("🤖 Mini GPT")

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
query = st.chat_input("Ask something...")

if query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    # 🔥 Build conversation context (last 5 messages)
    conversation = ""
    for msg in st.session_state.messages[-5:]:
        conversation += f"{msg['role']}: {msg['content']}\n"

    # 🔥 Route query
    agent = route_query(query)

    if agent == "calculator":
        answer = calculator_tool(query)

    elif agent == "rag":
        context = retrieve(query, embed_model, index, documents)

        prompt = f"""
You are a helpful AI assistant.

Conversation:
{conversation}

Use the context only if useful.

Context:
{context}

Question:
{query}

Answer:
"""
        result = pipe(prompt)[0]["generated_text"]
        answer = clean_output(result)

    else:
        prompt = f"""
Conversation:
{conversation}

Question:
{query}

Answer:
"""
        result = pipe(prompt)[0]["generated_text"]
        answer = clean_output(result)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)