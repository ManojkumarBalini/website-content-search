# ⚙️ Backend - Website Content Search

This is the **backend service** for the **Website Content Search** application.  
It powers the frontend with APIs for **HTML parsing**, **text tokenization**, and **vector-based content search** using **FastAPI**.

---

## 🚀 Overview

The backend is designed to:
- Parse and clean HTML web page data 🧹  
- Tokenize content and generate vector embeddings 🔠  
- Perform semantic search on processed website data 🧠  
- Serve data efficiently to the React frontend via REST API 🔗  

---

## 📁 Directory Structure

```

backend/
├── app/
│   ├── main.py              # Entry point for FastAPI
│   ├── models.py            # Data models (if any)
│   ├── services/
│   │   ├── html_parser.py   # Extracts text from HTML
│   │   ├── tokenizer.py     # Splits text into tokens
│   │   └── vector_search.py # Performs similarity-based search
│   ├── **init**.py
│   └── **pycache**/
├── requirements.txt         # Python dependencies
└── start.sh                 # Script to run the backend

````

---

## 🧩 Technologies Used

- **FastAPI** — For creating APIs  
- **Python 3.11+** — Core backend language  
- **BeautifulSoup / lxml** — For HTML parsing  
- **NumPy / scikit-learn** — For vector computations  
- **Uvicorn** — ASGI server to run FastAPI  

---

## ⚙️ Setup and Installation

### 1️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start the Server

```bash
bash start.sh
```

or manually run:

```bash
uvicorn app.main:app --reload
```

Server runs at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧠 API Endpoints (Example)

| Endpoint      | Method | Description                       |
| ------------- | ------ | --------------------------------- |
| `/parse_html` | POST   | Parses HTML and extracts content  |
| `/tokenize`   | POST   | Tokenizes text for vectorization  |
| `/search`     | POST   | Performs vector similarity search |

---

## 🧑‍💻 Author

**Manoj Kumar**
Backend Developer | AI & Full Stack Enthusiast

---

## 🪪 License

This project is licensed under the **MIT License** — free to use and modify.
