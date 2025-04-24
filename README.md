# 🧵 ThreadSeekerAI

**ThreadSeekerAI** is a semantic search engine that finds intelligent, interesting, and vibe-matching threads based on natural language queries. Whether you're looking for "deep convos about AI ethics with humor" or "threads on creative tech for introverts", this tool delivers smart, ranked results with explainable AI.

---

## 🚀 Features

- 🔍 Natural language search for threads
- 🧠 SentenceTransformer-based semantic similarity
- 💬 Ranked results with title, content, and tags
- 🛠️ Clean Flask API (`/search`) with CORS
- ⚡ Streamlit-powered frontend for quick interaction
- 🧪 Unit-test ready backend logic

---

## 🛠️ Tech Stack

| Layer       | Tech                                |
|-------------|-------------------------------------|
| Frontend    | Streamlit                           |
| Backend API | Flask + Flask-CORS                  |
| NLP Model   | SentenceTransformer (`MiniLM-L6-v2`)|
| Data        | JSON thread mock dataset            |
| Dev Tools   | Thunder Client / Postman, Git       |

---

## 📦 Folder Structure

ThreadSeekerAI/
├── test_run.py   
├── app_frontend.py    
├── backend/
│   ├── similarity.py
│   └── thread_data.json
├── tests/
│   └── test_similarity.py
├── requirements.txt
├── README.md
...

