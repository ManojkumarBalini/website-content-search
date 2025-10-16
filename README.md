# 🌐 Website Content Search

A full-stack web application that allows users to **search and analyze website content** efficiently using **vector-based search and HTML parsing**.  
This project integrates a **Python FastAPI backend** with a **ReactJS frontend** to provide a seamless search experience.

---

## 🚀 Features

- 🔍 Extracts and parses text from web pages using custom HTML parsers.  
- 🧠 Tokenizes content and performs semantic similarity search using vector embeddings.  
- ⚡ Fast, real-time search results through optimized backend services.  
- 💻 Simple and responsive React frontend for easy interaction.  
- 🧩 Modular architecture for scalability and maintainability.

---

## 🏗️ Project Structure

```

website-content-search/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── models.py            # Database or data models
│   │   ├── services/            # Core backend logic
│   │   │   ├── html_parser.py
│   │   │   ├── tokenizer.py
│   │   │   └── vector_search.py
│   ├── requirements.txt         # Python dependencies
│   └── start.sh                 # Backend start script
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
└── README.md

````

---

## ⚙️ Installation and Setup

### 1️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
bash start.sh
````

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Then open: **[http://localhost:3000](http://localhost:3000)**

---

## 🧠 Technologies Used

* **Backend:** FastAPI, Python
* **Frontend:** ReactJS, JavaScript, CSS
* **Search Logic:** Tokenization & Vector Embedding
* **Tools:** HTML Parser, REST API, JSON

---

## 📸 Preview

A clean and minimal interface to search and view website content results.

---

## 🧑‍💻 Author

**Manoj Kumar**
Full-Stack Developer | AI Enthusiast

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify it.
