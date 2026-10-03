<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,35:1e293b,65:4f46e5,100:06b6d4&height=220&section=header&text=MINI-GPT&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=34&desc=FINE-TUNED%20LLM%20%E2%80%A2%20RAG%20%E2%80%A2%20MULTI-AGENT%20AI&descSize=17&descAlignY=57&descColor=ffffff"
    width="100%"
    alt="Mini-GPT"
  />
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=900&color=4F46E5&center=true&vCenter=true&repeat=true&width=760&height=34&lines=Fine-Tuned+TinyLlama+1.1B;LoRA%2FPEFT+%7C+RAG+%7C+FAISS;Multi-Agent+Query+Routing;Retrieval-Augmented+Generation;End-to-End+Generative+AI+Application"
    alt="Mini-GPT capabilities"
  />
</p>

<p align="center">
  <kbd>TINYLLAMA 1.1B</kbd>
  &nbsp;&nbsp;
  <kbd>LoRA / PEFT</kbd>
  &nbsp;&nbsp;
  <kbd>RAG</kbd>
  &nbsp;&nbsp;
  <kbd>FAISS</kbd>
  &nbsp;&nbsp;
  <kbd>MULTI-AGENT</kbd>
</p>

🧠 What is Mini-GPT?
Mini-GPT is an end-to-end Generative AI application built around a fine-tuned TinyLlama 1.1B language model.
The project combines LoRA/PEFT fine-tuning, Retrieval-Augmented Generation (RAG), FAISS vector search, multi-agent query routing, conversation memory, and Streamlit into a single interactive AI system.
Rather than relying on a language model alone, Mini-GPT uses specialized components to determine how different types of queries should be processed — from direct LLM responses and knowledge retrieval to mathematical calculations.
<p align="center">
  <kbd>USER QUERY</kbd>
  &nbsp;→&nbsp;
  <kbd>ROUTER</kbd>
  &nbsp;→&nbsp;
  <kbd>SPECIALIZED AGENT</kbd>
  &nbsp;→&nbsp;
  <kbd>AI RESPONSE</kbd>
</p>

Deployment note: The online demo runs on limited cloud resources, so response generation may be slower than local execution. The project can also be run locally using the installation instructions below.

📸 Project Preview
Mini-GPT Interactive Interface
<p align="center">
  <img
    width="1919"
    height="953"
    alt="Mini-GPT interactive interface"
    src="https://github.com/user-attachments/assets/699e99f2-ca1a-4abc-b76b-3a46481b6c88"
  />
</p>

🚀 Live Demo
<p align="center">
  <a href="https://mini-gpt-wsjad3mp75fpdpsgdapp9ht.streamlit.app/">
    <kbd>🌐 OPEN MINI-GPT ONLINE →</kbd>
  </a>
</p>

The online demo is hosted on Streamlit Community Cloud. Because the application performs LLM inference using TinyLlama on limited cloud resources, response generation may be slower than the local version. For the best performance and complete functionality, local execution is recommended.

📌 Project Overview
Mini-GPT is an experimental AI assistant designed to demonstrate how modern Large Language Model applications can combine multiple AI techniques rather than relying on a language model alone.
🧩 System Components
Component	Role
🤖 Fine-Tuned LLM	Generates responses using the adapted TinyLlama model
🎓 LoRA / PEFT	Parameter-efficient model adaptation
📚 RAG	Retrieves relevant external knowledge
🔎 FAISS	Performs vector similarity search
🧠 Multi-Agent Routing	Directs queries to specialized components
🧮 Calculator Agent	Handles basic mathematical queries
💬 Conversation Memory	Maintains recent conversation context
🖥️ Streamlit	Provides the interactive web interface


🎯 Project Objectives
The main objectives of the project were:
- Build and fine-tune a lightweight language model.
- Train the model on a custom dataset.
- Integrate external knowledge retrieval using RAG.
- Implement vector similarity search using FAISS.
- Create multiple specialized agents for different tasks.
- Dynamically route user queries to the appropriate agent.
- Maintain conversation context through chat memory.
- Build an interactive user interface using Streamlit.
- Make the complete system executable locally and deployable as a web application.
🧠 System Architecture
The Mini-GPT architecture combines query routing, specialized agents, retrieval, and fine-tuned generation into a single request-processing pipeline.
<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=17&pause=800&color=4F46E5&center=true&vCenter=true&repeat=true&width=800&height=38&lines=USER+QUERY+%E2%86%92+STREAMLIT+UI+%E2%86%92+QUERY+ROUTER;QUERY+ROUTER+%E2%86%92+LLM+AGENT+%7C+RAG+AGENT+%7C+CALCULATOR+AGENT;RAG+AGENT+%E2%86%92+SENTENCE+TRANSFORMER+%E2%86%92+FAISS;FAISS+%E2%86%92+RETRIEVED+CONTEXT+%E2%86%92+TINYLLAMA+%2B+LoRA;TINYLLAMA+%2B+LoRA+%E2%86%92+AI+RESPONSE"
    alt="Animated Mini-GPT system architecture"
  />
</p>

<p align="center">
  <kbd>USER QUERY</kbd>
  &nbsp;→&nbsp;
  <kbd>QUERY ROUTER</kbd>
  &nbsp;→&nbsp;
  <kbd>SPECIALIZED AGENT</kbd>
  &nbsp;→&nbsp;
  <kbd>AI RESPONSE</kbd>
</p>

<p align="center">
  <sub>
    Specialized routing → retrieval when required → grounded context → fine-tuned generation
  </sub>
</p>

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
Hugging Face Hub	Model and adapter hosting


🤖 LLM & Fine-Tuning
Mini-GPT is built around TinyLlama/TinyLlama-1.1B-Chat-v1.0, a lightweight language model used as the foundation for the application.
<p align="center">
  <kbd>TINYLLAMA 1.1B</kbd>
  &nbsp;→&nbsp;
  <kbd>LoRA</kbd>
  &nbsp;→&nbsp;
  <kbd>PEFT ADAPTER</kbd>
  &nbsp;→&nbsp;
  <kbd>GENERATIVE AI</kbd>
</p>

🧠 Base Language Model
The project uses:
TinyLlama/TinyLlama-1.1B-Chat-v1.0
The base model is loaded first and the trained LoRA adapter is then attached to it during application startup.
🎓 LoRA / PEFT Fine-Tuning
Instead of modifying the entire TinyLlama model, Mini-GPT uses Low-Rank Adaptation (LoRA) through Parameter-Efficient Fine-Tuning (PEFT).
LoRA introduces a comparatively small set of trainable parameters while keeping the original model largely frozen.
Why LoRA?
Benefit	Description
💾 Lower Memory Usage	Requires fewer trainable parameters than full fine-tuning
⚡ Efficient Training	Reduces the computational requirements of adaptation
📦 Smaller Adapter	The trained adapter can be stored separately from the base model
🔄 Easy Integration	The adapter can be loaded on top of the base TinyLlama model
🖥️ Practical Experimentation	Suitable for experimenting with model adaptation on limited hardware


🔗 Fine-Tuned Adapter
The trained LoRA adapter is hosted separately on Hugging Face:
jatin-verma-ai/intelliagent-model
The application loads the adapter using PEFT:
model = PeftModel.from_pretrained(
    model,
    "jatin-verma-ai/intelliagent-model"
)
This keeps the trained adapter outside the GitHub repository while allowing the application to retrieve it when required.
📊 Training Dataset
The Mini-GPT model was fine-tuned using a custom dataset containing approximately 14K training samples.
The dataset was prepared specifically for the project to provide examples suitable for adapting the language model toward the desired response patterns.
📦 Dataset Overview
Property	Details
🧾 Dataset Type	Custom fine-tuning dataset
📊 Training Samples	~14K
🤖 Base Model	TinyLlama 1.1B
🎓 Fine-Tuning Method	LoRA / PEFT
📦 Output	Trained LoRA Adapter


🔄 Training Flow
<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=850&color=4F46E5&center=true&vCenter=true&repeat=true&width=760&height=36&lines=CUSTOM+DATASET+%E2%86%92+14K%2B+TRAINING+SAMPLES;TRAINING+DATASET+%E2%86%92+TINYLLAMA+1.1B;TINYLLAMA+%E2%86%92+LoRA%2FPEFT+FINE-TUNING;FINE-TUNING+%E2%86%92+TRAINED+ADAPTER;TRAINED+ADAPTER+%E2%86%92+HUGGING+FACE"
    alt="Mini-GPT training workflow"
  />
</p>

<p align="center">
  <kbd>DATASET</kbd>
  &nbsp;→&nbsp;
  <kbd>TINYLLAMA</kbd>
  &nbsp;→&nbsp;
  <kbd>LoRA / PEFT</kbd>
  &nbsp;→&nbsp;
  <kbd>ADAPTER</kbd>
  &nbsp;→&nbsp;
  <kbd>HUGGING FACE</kbd>
</p>

The trained adapter is hosted separately on Hugging Face rather than being stored directly inside the GitHub repository. This keeps the repository lightweight while allowing the application to retrieve the adapter when required.
🔄 Retrieval-Augmented Generation (RAG)
Fine-tuning adapts the language model's response behavior, while Retrieval-Augmented Generation (RAG) provides a mechanism for retrieving relevant external knowledge during inference.
Mini-GPT uses SentenceTransformers + FAISS to retrieve relevant context before generating an answer with TinyLlama.
🧠 RAG Pipeline
<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=850&color=4F46E5&center=true&vCenter=true&repeat=true&width=800&height=38&lines=USER+QUERY+%E2%86%92+QUERY+EMBEDDING;QUERY+EMBEDDING+%E2%86%92+FAISS+VECTOR+SEARCH;FAISS+VECTOR+SEARCH+%E2%86%92+RELEVANT+CONTEXT;RELEVANT+CONTEXT+%2B+QUERY+%E2%86%92+TINYLLAMA+%2B+LoRA;TINYLLAMA+%2B+CONTEXT+%E2%86%92+GENERATED+ANSWER"
    alt="Animated Mini-GPT RAG pipeline"
  />
</p>

<p align="center">
  <kbd>USER QUERY</kbd>
  &nbsp;→&nbsp;
  <kbd>EMBEDDING</kbd>
  &nbsp;→&nbsp;
  <kbd>FAISS</kbd>
  &nbsp;→&nbsp;
  <kbd>CONTEXT</kbd>
  &nbsp;→&nbsp;
  <kbd>TINYLLAMA</kbd>
  &nbsp;→&nbsp;
  <kbd>ANSWER</kbd>
</p>

🔢 Sentence Transformers
Mini-GPT uses:
all-MiniLM-L6-v2
from SentenceTransformers.
Documents are converted into numerical vector representations called embeddings.
When a user submits a query, the query is also converted into an embedding. The system then compares the query embedding against the stored document embeddings to identify relevant information.
🔎 FAISS Vector Search
FAISS (Facebook AI Similarity Search) is used as the vector search engine.
The project creates:
faiss.IndexFlatL2
The query embedding is compared against the stored embeddings using L2 distance, and the most relevant document is retrieved.
The retrieved information is then inserted into the prompt provided to TinyLlama.
📌 RAG in Mini-GPT
User Query
     ↓
Sentence Transformer
     ↓
Query Embedding
     ↓
FAISS Vector Search
     ↓
Relevant Context
     ↓
TinyLlama + LoRA
     ↓
Generated Answer
<p align="center">
  <sub>
    Retrieval provides relevant context that can be incorporated into the generation process.
  </sub>
</p>

🤝 Multi-Agent System
Instead of sending every user request directly to the language model, Mini-GPT implements a simple multi-agent routing system.
The system currently contains three logical agents:
🧠 LLM Agent
Handles general questions that do not require a specialized tool or retrieval pipeline.
📚 RAG Agent
Handles knowledge-oriented queries such as:
What is...?
Explain...
Define...
Why...?
How does...?
The agent retrieves relevant information through SentenceTransformers + FAISS before generating the response.
🧮 Calculator Agent
Handles basic mathematical queries.
Example:
25 * 16
The query is routed directly to the calculator rather than unnecessarily sending it through the LLM.
🔀 Query Routing
The routing logic determines which agent should process a query.
<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&pause=850&color=4F46E5&center=true&vCenter=true&repeat=true&width=760&height=36&lines=USER+QUERY+%E2%86%92+QUERY+ROUTER;MATHEMATICAL+QUERY+%E2%86%92+CALCULATOR+AGENT;KNOWLEDGE+QUERY+%E2%86%92+RAG+AGENT;OTHER+QUERY+%E2%86%92+LLM+AGENT"
    alt="Mini-GPT query routing"
  />
</p>

Query Type	Route
Mathematical query	Calculator Agent
Knowledge-oriented query	RAG Agent
Other query	LLM Agent


This demonstrates the basic principle behind tool-using and agent-based AI systems: different tasks can be handled by specialized components instead of forcing a single model to perform every operation.
💬 Conversation Memory
Mini-GPT maintains conversation history using:
st.session_state
User and assistant messages are stored in Streamlit's session state.
Recent conversation messages are included in subsequent prompts, allowing the model to maintain some context during multi-turn conversations.
Example
User: What is machine learning?

Assistant: Machine learning is...

User: How is it different from traditional programming?

Assistant: ...
The stored conversation context allows subsequent queries to retain some awareness of the ongoing conversation.
🖥️ Streamlit Interface
The application uses Streamlit to provide an interactive chat interface.
Interface Components
Component	Purpose
💬 Chat History	Displays the conversation
⌨️ User Input	Accepts user queries
🗨️ Message Bubbles	Separates user and assistant messages
⏳ Loading Indicator	Indicates processing
🤖 Model Responses	Displays generated answers
🧠 Session Memory	Maintains conversation context


The application can be launched locally using:
streamlit run app.py
⚙️ Model Loading & Caching
The project uses:
@st.cache_resource
for expensive model-loading operations.
This prevents Streamlit from unnecessarily loading the LLM and RAG components repeatedly during normal application reruns.
🔄 LLM Loading Pipeline
<p align="center">
  <kbd>TINYLLAMA</kbd>
  &nbsp;→&nbsp;
  <kbd>TOKENIZER</kbd>
  &nbsp;→&nbsp;
  <kbd>BASE MODEL</kbd>
  &nbsp;→&nbsp;
  <kbd>LORA ADAPTER</kbd>
  &nbsp;→&nbsp;
  <kbd>EVAL MODE</kbd>
  &nbsp;→&nbsp;
  <kbd>PIPELINE</kbd>
</p>

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
Repository Components
Component	Purpose
app.py	Complete application logic
app_backup.py	Local backup of the application
requirements.txt	Python dependencies
screenshots/	Project screenshots
README.md	Documentation
.gitignore	Git ignore configuration


💻 Requirements
Recommended Environment
Requirement	Details
🐍 Python	3.11
🌱 Environment	Conda or virtual environment
🌐 Internet	Required for downloading models and the LoRA adapter
💾 Hardware	Sufficient RAM for loading TinyLlama and supporting libraries


Main Dependencies
streamlit
torch
transformers
peft
huggingface-hub
sentence-transformers
faiss-cpu
numpy
🚀 Installation
1. Clone the Repository
git clone https://github.com/jv906699/Mini-GPT.git
2. Enter the Project Directory
cd Mini-GPT
3. Create a Conda Environment
conda create -n intelliagent python=3.11
4. Activate the Environment
conda activate intelliagent
5. Install Dependencies
pip install -r requirements.txt
▶️ Running the Application
Start Streamlit:
streamlit run app.py
Streamlit will provide a local URL, normally:
http://localhost:8501
Open the displayed URL in your browser.
🤗 Fine-Tuned Model
The trained LoRA adapter is hosted on Hugging Face:
jatin-verma-ai/intelliagent-model
The application automatically loads the adapter through:
PeftModel.from_pretrained(
    model,
    "jatin-verma-ai/intelliagent-model"
)
Therefore, the trained model files do not need to be stored directly inside the GitHub repository.
🌐 Online Demo
The project is also available as an online Streamlit application.
<p align="center">
  <a href="https://mini-gpt-wsjad3mp75fpdpsgdapp9ht.streamlit.app/">
    <kbd>🚀 TRY MINI-GPT ONLINE →</kbd>
  </a>
</p>

Performance note: The online version currently runs on limited cloud resources, so response generation may be slower than the local version. Local installation is recommended for testing the complete system.

🧪 Example Queries
🧠 General LLM
Tell me about artificial intelligence.
Route: LLM Agent
📚 RAG
What is overfitting?
Route: RAG Agent
🧮 Calculator
25 * 16
Route: Calculator Agent
💬 Multi-Turn Conversation
User: What is machine learning?

Assistant: ...

User: How does it learn?

Assistant: ...
Context: Stored conversation history

📈 Key Features
- ✅ Fine-tuned TinyLlama 1.1B
- ✅ LoRA / PEFT fine-tuning
- ✅ Custom ~14K-sample dataset
- ✅ Retrieval-Augmented Generation
- ✅ SentenceTransformer embeddings
- ✅ FAISS vector search
- ✅ Multi-agent query routing
- ✅ Calculator tool
- ✅ Conversation memory
- ✅ Streamlit interactive UI
- ✅ Hugging Face model hosting
- ✅ Local execution
- ✅ Online demonstration
🧠 What This Project Demonstrates
Mini-GPT demonstrates practical implementation of several components used in modern Generative AI applications:
Area	Implementation
🤖 Large Language Models	TinyLlama 1.1B
🎓 Parameter-Efficient Fine-Tuning	LoRA / PEFT
📚 Retrieval-Augmented Generation	SentenceTransformers + FAISS
🔎 Vector Similarity Search	FAISS IndexFlatL2
🧠 Embeddings	all-MiniLM-L6-v2
🤝 Agent-Based Task Routing	LLM / RAG / Calculator agents
🧮 Tool Integration	Calculator agent
💬 Conversation Memory	Streamlit st.session_state
🖥️ LLM Application Development	Streamlit
☁️ Model Hosting	Hugging Face Hub
🚀 Deployment	Local + Streamlit Community Cloud

# 🔬 Technical Workflow

The following workflow shows how a request moves through Mini-GPT from the user interface to the final response.

```text
USER
  │
  ▼
Streamlit UI
  │
  ▼
Query Router
  │
  ├──────────────┬──────────────┐
  ▼              ▼              ▼
LLM Agent     RAG Agent    Calculator Agent
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
        TinyLlama + LoRA
                 │
                 ▼
           AI Response
                 │
                 ▼
          Chat History

Rather than building only a chatbot interface, the project combines model adaptation, retrieval, routing, tools, memory, and UI into a single end-to-end AI application.
🔮 Future Improvements
Potential improvements include:
- More sophisticated agent orchestration
- Larger and more diverse knowledge base
- Improved query classification
- Better conversation memory
- Streaming token generation
- GPU-accelerated online deployment
- Model quantization
- More advanced vector database integration
- Additional tools and agents
- Improved evaluation metrics
- Better hallucination detection
- Production-grade deployment infrastructure
👨‍💻 Author
<p align="center">
  <b>Jatin Kumar Verma</b>
  <br>
  B.Tech — Artificial Intelligence
</p>

<p align="center">
  <sub>
    Mini-GPT · TinyLlama · LoRA / PEFT · RAG · FAISS · Multi-Agent AI
  </sub>
</p>
