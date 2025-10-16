# 💻 Frontend - Website Content Search

This is the **frontend interface** of the **Website Content Search** application.  
It allows users to enter a website URL, search for specific keywords, and view matching results with highlighted HTML content and match percentages.

---

## 🚀 Overview

The frontend is built using **ReactJS** and provides:
- 🌐 A clean and responsive user interface  
- 🔍 Input fields for URL and keyword search  
- 📄 Result cards showing titles, paths, and match scores  
- 🧩 A “View HTML” feature that displays raw HTML inside a formatted `<pre><code>` block  
- ⚡ Smooth integration with the backend FastAPI service

---

## 📁 Directory Structure

```

frontend/
├── public/
│   └── index.html                 # Root HTML file
├── src/
│   ├── components/
│   │   ├── SearchForm.js          # Handles user input and search submission
│   │   ├── SearchResults.js       # Displays the search results
│   │   └── LoadingSpinner.js      # Loading indicator during API requests
│   ├── App.js                     # Main app component
│   ├── App.css                    # App-level styles
│   ├── index.js                   # Entry point for React
│   └── index.css                  # Global styles
└── package.json                   # Project dependencies and scripts

````

---

## ⚙️ Setup and Installation

### 1️⃣ Install Dependencies
```bash
cd frontend
npm install
````

### 2️⃣ Run the Development Server

```bash
npm start
```

Then open your browser at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## 🧠 Technologies Used

* **ReactJS** — Component-based frontend framework
* **JavaScript (ES6+)** — Core logic
* **HTML5 & CSS3** — Structure and styling
* **Axios / Fetch API** — For connecting with the FastAPI backend

---

## 🧑‍💻 Author

**Manoj Kumar**
Frontend Developer | Full Stack & AI Enthusiast

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify.
