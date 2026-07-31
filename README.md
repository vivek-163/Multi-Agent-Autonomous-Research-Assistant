# 🤖 [Multi-Agent Autonomous Research System](https://multi-agent-autonomous-research-assistant.streamlit.app/)

A multi-agent AI research pipeline built with **LangChain**, **LCEL**, **OpenAI**, **Tavily Search API**, and **BeautifulSoup**.

The system autonomously researches a topic by coordinating multiple specialized AI agents that search the web, read webpages, generate a research report, and review the final output.

---

## 📖 Overview

This project demonstrates how multiple AI agents can collaborate through a **shared state dictionary** managed by a **Supervisor Pipeline**.

The workflow is:

1. 🔍 Search the Internet
2. 📄 Read and extract webpage content
3. ✍️ Generate a research report
4. ⭐ Critique and improve the report

---

# 🏗️ System Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/05f48588-a68b-4876-b9d7-8c1076db46d3" />


---

# 🚀 Features

- Multi-Agent Architecture
- Supervisor-based orchestration
- Tavily live web search
- Webpage scraping using BeautifulSoup
- Shared state management
- LangChain ReAct Agents
- LCEL Chains
- Automatic report generation
- AI-based report review
- Modular project structure

---

# 📂 Project Structure

```
multi-agent-research/
│
├── tools.py
├── agents.py
├── pipeline.py
├── requirements.txt
├── .env
│
└── README.md
```

---

# ⚙️ Workflow

```
User
 │
 ▼
Research Topic
 │
 ▼
Search Agent
 │
 ▼
Tavily Search API
 │
 ▼
Search Results
 │
 ▼
Reader Agent
 │
 ▼
BeautifulSoup
 │
 ▼
Clean Documents
 │
 ▼
Writer Chain
 │
 ▼
Research Report
 │
 ▼
Critic Chain
 │
 ▼
Feedback + Score
```

---

# 🧠 Agents

## 1️⃣ Search Agent

**Purpose**

Searches the internet for relevant information.

**Framework**

- create_react_agent
- AgentExecutor

**Tool**

```
web_search_tool()
```

**Output**

```python
state["search_results"]
```

---

## 2️⃣ Reader Agent

**Purpose**

Visits webpages and extracts readable content.

**Framework**

- create_react_agent
- AgentExecutor

**Tool**

```
scrape_url_tool()
```

Uses:

- BeautifulSoup
- Requests

**Output**

```python
state["documents"]
```

---

## 3️⃣ Writer Chain

Creates the final research report.

LCEL Pipeline

```
Prompt
    │
    ▼
LLM
    │
    ▼
StrOutputParser()
```

Output

```python
state["report"]
```

---

## 4️⃣ Critic Chain

Reviews the generated report.

Provides

- Score
- Strengths
- Weaknesses
- Suggestions

Output

```python
state["review"]
```

---

# 🔄 Shared State

Every agent communicates through a single shared dictionary.

```python
state = {

    "topic": "",

    "search_results": [],

    "documents": [],

    "report": "",

    "review": {}

}
```

---

# 🛠 Tools

## Tool 1

### web_search_tool()

Uses

- Tavily API

Returns

- URLs
- Search snippets
- Sources

---

## Tool 2

### scrape_url_tool()

Uses

- BeautifulSoup

Returns

- Clean webpage text

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/vivek-163/Multi-Agent-Autonomous-Research-Assistant.git
```

Move into the project

```bash
cd multi-agent-research
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
OPENAI_API_KEY=your_key_here (you can also use Groq cloud api key)

TAVILY_API_KEY=your_key_here
```

---

# ▶️ Running

```bash
python pipeline.py
```

Example

```
Enter research topic:

Future of Quantum Computing
```

---

# 📊 Pipeline Execution

```
Search Agent
      │
      ▼
Reader Agent
      │
      ▼
Writer Chain
      │
      ▼
Critic Chain
```

Each stage updates the shared state.

---

# 🖥 Example Output

```
Topic:
Future of Quantum Computing

Searching...

Reading URLs...

Generating Report...

Reviewing Report...

================================

Research Report

================================

Score: 9.2/10

Suggestions:

• Add more recent citations

• Include future trends

• Improve conclusion
```

---

# 🧩 Tech Stack

- Python
- LangChain
- LCEL
- OpenAI
- Tavily Search API
- BeautifulSoup
- Requests
- dotenv

---

# 🎯 Future Improvements

- Multi-threaded agents
- Memory module
- RAG integration
- Vector Database
- PDF export
- Markdown export
- Streamlit UI
- LangGraph implementation

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙌 Acknowledgements

- OpenAI
- LangChain
- Tavily
- BeautifulSoup
