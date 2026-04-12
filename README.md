#  Mini GPT – AI Assistant with LLM + RAG + Multi-Agent System

Mini GPT is a lightweight AI assistant built using a fine-tuned Large Language Model (LLM), Retrieval-Augmented Generation (RAG), and a simple multi-agent system.
It can answer theoretical questions, perform calculations, and maintain conversational context.

---

##  Features

*  Fine-tuned LLM (TinyLlama + LoRA)
*  RAG (Retrieval-Augmented Generation using FAISS)
*  Multi-Agent System:

  * Calculator Agent
  * Knowledge (RAG) Agent
  * General LLM Agent
* Chat Memory (context-aware responses)
*  Streamlit UI

---

##  Architecture

User Query
→ Query Routing
→ Selected Agent (Calculator / RAG / LLM)
→ Response Generation
→ Chat Memory Update

---

##  Model Details

* Base Model: TinyLlama-1.1B-Chat
* Fine-tuning: LoRA (PEFT)
* Hosted on Hugging Face:

 https://huggingface.co/jatin-verma-ai/intelliagent-model

---

##  Requirements

Make sure you have:

* Python 3.10+
* pip / conda

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/jv906699/Mini-GPT.git
cd Mini-GPT
```

### 2. Create virtual environment (recommended)

```bash
conda create -n mini-gpt python=3.10
conda activate mini-gpt
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Application

```bash
streamlit run app.py
```

Then open:

http://localhost:8501

---

##  Example Queries

* What is machine learning?
* Explain gradient descent
* What is overfitting?
* 25 * 67
* Why are neural networks used?

---

##  How It Works

###  Query Routing

* Math → Calculator agent
* Theory → RAG agent
* Others → LLM

###  RAG

* Uses SentenceTransformers for embeddings
* FAISS for similarity search

###  Chat Memory

* Stores recent conversation
* Improves context understanding

---

##  Limitations

* Small model (1.1B) → limited reasoning
* RAG dataset is currently small
* Slower performance on CPU

---

##  Future Improvements

* Add coding dataset
* Add current affairs knowledge
* Improve response speed
* Add more intelligent agents

---

##  Demo

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/40546ea7-3ed1-4246-8c03-b769b3081682" />


---

##  Author

Jatin Verma
B.Tech AI Student
AI/ML Enthusiast

---

##  If you like this project

Give it a star  on GitHub!
 
