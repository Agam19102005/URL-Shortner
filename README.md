# 🔗 URL Shortener (Bitly Clone)

A full-stack URL shortening service built using Flask that converts long URLs into short, shareable links with analytics support.

---

## 🚀 Live Demo

👉 https://your-app-name.onrender.com

---

## 📌 Features

* 🔗 Shorten long URLs instantly
* ✨ Custom short URLs (user-defined aliases)
* ⚠️ Collision handling (prevents duplicate short codes)
* 📊 Click analytics tracking
* 🔄 Automatic redirection
* 🎨 Simple and clean UI

---

## 🧠 Tech Stack

| Layer      | Technology     |
| ---------- | -------------- |
| Backend    | Python (Flask) |
| Database   | SQLite         |
| Frontend   | HTML, CSS      |
| Deployment | Render         |
| Server     | Gunicorn       |

---

## ⚙️ How It Works

1. User enters a long URL
2. System generates a unique short code using **Base62 encoding**
3. Mapping is stored in the database
4. Short URL redirects to original URL
5. Each visit updates click analytics

---

## 📊 Example

**Input:**
https://google.com

**Output:**
https://your-app-name.onrender.com/u/b

---

## 🧠 Core Concepts Used

* Hashing
* Base62 Encoding
* Database Design (Mapping + Indexing)
* Collision Handling
* RESTful Routing
* System Design Basics

---

## 📁 Project Structure

```
url-shortener/
│
├── app.py
├── requirements.txt
├── Procfile
├── database.db
│
├── templates/
│   ├── index.html
│   └── stats.html
│
└── README.md
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
pip install -r requirements.txt
python app.py
```

Open:
http://127.0.0.1:5000/

---

## 🌍 Deployment

This project is deployed on Render using Gunicorn.

Steps:

1. Push code to GitHub
2. Create a Web Service on Render
3. Add:

   * Build: `pip install -r requirements.txt`
   * Start: `gunicorn app:app`

---

## 🚀 Future Improvements

* 🔐 User authentication
* ⚡ Redis caching for faster lookup
* 📅 Expiring links
* 📈 Advanced analytics (geo, device)
* 🌐 Custom domains

---

## 💥 Challenges Faced

* Handling route conflicts (`/u/` vs `/stats/`)
* Avoiding duplicate short codes
* Designing scalable URL mapping system

---

## 🧠 Interview Highlights

* Designed a URL shortening system using hashing and Base62 encoding
* Achieved O(1) lookup using database indexing
* Implemented collision handling and custom alias support
* Built analytics tracking for each URL

---

## 👨‍💻 Author

**Agam Kadakia**
BTech CSE (AI & Edge Computing)

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub!
