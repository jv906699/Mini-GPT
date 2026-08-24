🤖 Mini GPT — AI Assistant with LLM, RAG & Multi-Agent System

A lightweight AI assistant built using a fine-tuned TinyLlama 1.1B language model, LoRA/PEFT, Retrieval-Augmented Generation (RAG), FAISS, and a simple multi-agent architecture. The project combines model fine-tuning, retrieval-based knowledge augmentation, task routing, conversation memory, and an interactive Streamlit interface into a single AI application.

Note: The online demo currently runs on limited cloud resources and may respond slowly. For the best experience, run the project locally using the instructions provided below.

📸 Project Preview

Mini GPT interactive interface:

<img width="1919" height="953" alt="image" src="https://github.com/user-attachments/assets/699e99f2-ca1a-4abc-b76b-3a46481b6c88" />


🚀 Live Demo
🌐 Try Mini GPT Online

👉 Open the Live Demo

Note: The online demo is currently hosted on Streamlit Community Cloud. Because the application performs LLM inference using TinyLlama on limited cloud resources, response generation may be slower than the local version. For the best performance and complete functionality, it is recommended to run the project locally.

https://mini-gpt-wsjad3mp75fpdpsgdapp9ht.streamlit.app/

📌 Project Overview

Mini GPT is an experimental AI assistant designed to demonstrate how modern Large Language Model (LLM) applications can combine multiple AI techniques rather than relying on a language model alone.

The system integrates:

Fine-tuned Large Language Model
Parameter-Efficient Fine-Tuning (PEFT)
LoRA
Retrieval-Augmented Generation (RAG)
Sentence Transformers
FAISS vector search
Multi-agent query routing
Calculator tool
Conversation memory
Streamlit web interface

The objective was to build a compact but complete AI assistant that demonstrates the core components used in modern LLM applications.

🎯 Project Objectives

The main objectives of the project were:

Build and fine-tune a lightweight language model.
Train the model on a custom dataset.
Integrate external knowledge retrieval using RAG.
Implement vector similarity search using FAISS.
Create multiple specialized agents for different tasks.
Dynamically route user queries to the appropriate agent.
Maintain conversation context through chat memory.
Build an interactive user interface using Streamlit.
Make the complete system executable locally and deployable as a web application.
🧠 System Architecture

The overall system follows this workflow:

                    User Query
                        │
                        ▼
                ┌─────────────────┐
                │ Streamlit  UI   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Query Router   │
                └───────┬─────────┘
                        │
             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼
        Calculator     RAG        LLM
          Agent       Agent      Agent
             │          │          │
             │          ▼          │
             │    Sentence         │
             │    Transformer      │
             │          │          │
             │          ▼          │
             │       FAISS         │
             │          │          │
             │          ▼          │
             │       Context       │
             │          │          │
             └──────────┼──────────┘
                        ▼
                Fine-Tuned TinyLlama
                        │
                        ▼
                    AI Response
🧩 Technologies Used
Technology	Purpose
Python	Core programming language
TinyLlama 1.1B	Base language model
LoRA	Parameter-efficient fine-tuning
PEFT	Loading and managing LoRA adapters
Transformers	Model and tokenizer implementation
SentenceTransformers	Text embeddings
FAISS	Vector similarity search
NumPy	Numerical operations
Streamlit	Interactive web interface
Hugging Face Hub	Model/adapter hosting
🤖 Large Language Model

The project uses:

TinyLlama/TinyLlama-1.1B-Chat-v1.0

TinyLlama is a lightweight language model containing approximately 1.1 billion parameters and is suitable for experimentation and development on relatively limited hardware.

The base model was not used completely unchanged. A custom LoRA adapter was trained and later loaded on top of the base TinyLlama model.

🎓 Model Fine-Tuning
Why Fine-Tuning?

The objective of fine-tuning was to adapt the base language model to the desired response patterns using a custom training dataset.

Instead of training the entire model from scratch, the project uses Parameter-Efficient Fine-Tuning (PEFT).

LoRA / PEFT

LoRA (Low-Rank Adaptation) was used for fine-tuning.

Rather than modifying every parameter of TinyLlama, LoRA introduces a comparatively small number of trainable parameters while keeping the original model largely frozen.

This provides several advantages:

Lower memory requirements
Faster training
Smaller trained model files
Easier model distribution
Practical fine-tuning on consumer hardware

The trained adapter is hosted separately on Hugging Face:

jatin-verma-ai/intelliagent-model

The application loads the base model first and then attaches the trained LoRA adapter:

model = PeftModel.from_pretrained(
    model,
    "jatin-verma-ai/intelliagent-model"
)

📊 Training Dataset

The model was fine-tuned using a custom dataset containing approximately 14K training samples.

The dataset was prepared specifically for the Mini GPT project to provide examples suitable for training the language model to generate the desired type of responses.

Dataset size: ~14K samples

The trained adapter was then uploaded to Hugging Face rather than storing the model weights directly inside the GitHub repository.

This keeps the GitHub repository lightweight while allowing the application to download the trained adapter when required.


🔄 Retrieval-Augmented Generation (RAG)

Fine-tuning alone does not provide a mechanism for dynamically retrieving external knowledge.

Therefore, the project also implements Retrieval-Augmented Generation (RAG).

The RAG pipeline consists of:

User Query
    │
    ▼
Sentence Transformer
    │
    ▼
Query Embedding
    │
    ▼
FAISS Vector Search
    │
    ▼
Relevant Context
    │
    ▼
TinyLlama
    │
    ▼
Generated Answer

🔢 Sentence Transformers

The project uses:

all-MiniLM-L6-v2

from SentenceTransformers.

The documents are converted into numerical vector representations called embeddings.

When a user asks a question, the question is also converted into an embedding.

The system then compares the query embedding against the stored document embeddings.

🔎 FAISS

FAISS (Facebook AI Similarity Search) is used as the vector database/search engine.

The project creates an:

faiss.IndexFlatL2

index.

The query embedding is compared against the stored embeddings using L2 distance, and the most relevant document is retrieved.

The retrieved information is then inserted into the prompt given to TinyLlama.

🤝 Multi-Agent System

Instead of sending every user request directly to the language model, Mini GPT implements a simple multi-agent routing system.

The system currently contains three logical agents:

1. 🧠 LLM Agent

Handles general questions that do not require a specialized tool or retrieval pipeline.

2. 📚 RAG Agent

Handles knowledge-oriented queries such as:

What is...?
Explain...
Define...
Why...?
How does...?

The agent retrieves relevant information through SentenceTransformers + FAISS before generating the response.

3. 🧮 Calculator Agent

Handles basic mathematical queries.

For example:

2 + 5

The query is routed directly to the calculator rather than unnecessarily sending it through the LLM.

🔀 Query Routing

The routing logic determines which agent should process a query.

Conceptually:

User Query
     │
     ▼
Query Router
     │
     ├── Mathematical query → Calculator Agent
     │
     ├── Knowledge query → RAG Agent
     │
     └── Other query → LLM Agent

This demonstrates the basic principle behind tool-using and agent-based AI systems: different tasks can be handled by specialized components instead of forcing a single model to perform every operation.

💬 Conversation Memory

Mini GPT maintains conversation history using:

st.session_state

User and assistant messages are stored in Streamlit's session state.

Recent conversation messages are included in subsequent prompts, allowing the model to maintain some context during multi-turn conversations.

Example:

User: What is machine learning?

Assistant: Machine learning is...

User: How is it different from traditional programming?

Assistant: ...

🖥️ Streamlit Interface

The application uses Streamlit to provide a simple interactive chat interface.

The interface includes:

Chat history
User input
User/assistant message bubbles
Loading indicator
Model responses
Persistent session-based conversation history

The application can be launched locally using:

streamlit run app.py

⚙️ Model Loading and Caching

The project uses:

@st.cache_resource

for expensive model-loading operations.

This prevents Streamlit from unnecessarily loading the LLM and RAG components repeatedly during normal application reruns.

The LLM loading pipeline is:

TinyLlama
    ↓
Load Tokenizer
    ↓
Load Base Model
    ↓
Load LoRA Adapter
    ↓
Evaluation Mode
    ↓
Transformers Pipeline
📁 Project Structure
Mini-GPT/
│
├── app.py
├── app_backup.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    └── mini-gpt-interface.png
app.py

Contains the complete application logic, including:

Model loading
LoRA adapter loading
RAG pipeline
FAISS search
Query routing
Calculator agent
Conversation memory
Streamlit UI
requirements.txt

Contains the Python dependencies required to run the project.

README.md

Project documentation, architecture, setup instructions, and usage information.

app_backup.py

A local backup of the application version maintained during development.

screenshots/

Contains screenshots used for project documentation.

💻 Requirements

Recommended environment:

Python 3.11
Conda or virtual environment
Internet connection for downloading models and the LoRA adapter
Sufficient RAM for loading TinyLlama and supporting libraries

Main Python dependencies:

streamlit
torch
transformers
peft
huggingface-hub
sentence-transformers
faiss-cpu
numpy

🚀 Installation

Clone the repository:

git clone https://github.com/jv906699/Mini-GPT.git

Enter the project directory:

cd Mini-GPT

Create a Conda environment:

conda create -n intelliagent python=3.11

Activate it:

conda activate intelliagent

Install dependencies:

pip install -r requirements.txt

▶️ Running the Application

Start Streamlit:

streamlit run app.py

Streamlit will provide a local URL, normally:

http://localhost:8501

Open the URL in your browser.

🤗 Fine-Tuned Model

The LoRA adapter is hosted on Hugging Face:

Model Repository:
jatin-verma-ai/intelliagent-model

The application automatically loads the adapter through:

PeftModel.from_pretrained(
    model,
    "jatin-verma-ai/intelliagent-model"
)

Therefore, the trained model files do not need to be stored directly inside the GitHub repository.

🌐 Online Demo

The project is also available as an online Streamlit application.

Live Demo

🚀 Try Mini GPT Online

Performance note: The online version currently runs on limited cloud resources, so response generation may be slower than the local version. The local installation is recommended for testing the complete system.

🧪 Example Queries
General LLM
Tell me about artificial intelligence.

→ Routed to the LLM Agent

RAG
What is overfitting?

→ Routed to the RAG Agent

Calculator
25 * 16

→ Routed to the Calculator Agent

Multi-turn conversation
User: What is machine learning?
Assistant: ...

User: How does it learn?
Assistant: ...

→ Uses the stored conversation context.

🔬 Technical Workflow

The complete request-processing pipeline is:

                  USER
                   │
                   ▼
             Streamlit UI
                   │
                   ▼
             Query Router
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   Calculator     RAG        LLM
     Agent       Agent      Agent
                  │
                  ▼
          SentenceTransformer
                  │
                  ▼
              Embedding
                  │
                  ▼
                FAISS
                  │
                  ▼
           Retrieved Context
                  │
                  ▼
              Prompt
                  │
                  ▼
       TinyLlama + LoRA Adapter
                  │
                  ▼
             AI Response
                  │
                  ▼
          Chat History
📈 Key Features
✅ Fine-tuned TinyLlama 1.1B
✅ LoRA / PEFT fine-tuning
✅ Custom ~14K-sample dataset
✅ Retrieval-Augmented Generation
✅ SentenceTransformer embeddings
✅ FAISS vector search
✅ Multi-agent query routing
✅ Calculator tool
✅ Conversation memory
✅ Streamlit interactive UI
✅ Hugging Face model hosting
✅ Local execution
✅ Online demonstration
🧠 What This Project Demonstrates

This project demonstrates practical implementation of several components used in modern Generative AI applications:

Large Language Models
Parameter-Efficient Fine-Tuning
LoRA
Retrieval-Augmented Generation
Vector similarity search
Embeddings
Agent-based task routing
Tool integration
Conversation memory
LLM application development
Model deployment

Rather than building only a chatbot interface, the project combines model training, retrieval, routing, tools, memory, and UI into a single end-to-end AI application.

🔮 Future Improvements

Potential improvements include:

More sophisticated agent orchestration
Larger and more diverse knowledge base
Improved query classification
Better conversation memory
Streaming token generation
GPU-accelerated online deployment
Model quantization
More advanced vector database integration
Additional tools and agents
Improved evaluation metrics
Better hallucination detection
Production-grade deployment infrastructure

👨‍💻 Author

Jatin Kumar Verma

B.Tech — Artificial Intelligence

