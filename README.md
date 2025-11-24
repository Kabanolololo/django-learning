# Django Learning Roadmap

Welcome to my Django learning repository! 🚀  
This repository is meant to track my progress while learning Django, from basics to creating a mini blog with HTML, API, and user authentication.

> **Note:** This roadmap was generated with ChatGPT and can be slightly modified as I go along.

---

## 📌 Roadmap

### ✅ ETAP 1 — Basics of Django (without database)
**🟢 Task 1: Create a Django project**
- Create project `myproject`
- Run local server
- Check the start page

**🟢 Task 2: Create "core" app**
- Create app: `core`
- Add a `home` view returning text: "Hello Django"
- Connect it in `urls.py`

**🟢 Task 3: Add second view**
- `/info` returns text: "This is information"
- Connect view to URL

---

### ✅ ETAP 2 — Database and Models
**🟡 Task 4: Create "Article" model**
- In `core` app, create model with:
  - `title` (CharField)
  - `content` (TextField)
  - `created_at` (DateTimeField, auto_now_add=True)

**🟡 Task 5: Migrations**
- Run `makemigrations`
- Run `migrate`

**🟡 Task 6: Add model to admin**
- Add `Article` to admin panel
- Log in and create 3 articles manually

**🟡 Task 7: Display list of articles as plain text**
- View `/articles`
- Fetch all articles from DB
- Return titles as text or list

📌 Practice Django ORM here.

---

### ✅ ETAP 3 — Endpoints / API (JSON)
**🔵 Task 8: JSON endpoint for articles list**
- URL: `/api/articles`
- Return JSON:  
```json
[
  {"id": 1, "title": "..."},
  {"id": 2, "title": "..."}
]
```

**🔵 Task 9: Article detail endpoint**
- URL: `/api/articles/<id>`
- Return full article JSON

**🔵 Task 10: Add article via POST**
- URL: `/api/articles/create`
- Accept `title`, `content`
- Create record
- Return JSON: `{ "created": 1 }`

**🔵 Task 11: Delete article**
- URL: `/api/articles/<id>/delete`
- Delete record
- Return JSON success info

📌 Can be done with plain Django or later with DRF.

---

### ✅ ETAP 4 — HTML Pages (Templates)
**🟣 Task 12: Create templates folder**
- Add `home.html` with simple HTML content
- Render template in view

**🟣 Task 13: Articles list in HTML**
- Page `/articles/html`
- Use `render(request, "articles.html", { ... })`
- Display articles in `<ul>`

**🟣 Task 14: Article detail page**
- Page `/article/<id>`
- Show title and content
- Add "Back" button

**🟣 Task 15: Article creation form**
- Page `/articles/new`
- HTML form + POST method
- After save → redirect to articles list

---

### 🔥 ETAP 5 — Integrating everything into one project
**🟥 Task 16: Create "blog" app**
- Move models, views, URLs into new app

**🟥 Task 17: Full CRUD with HTML**
- Articles:
  - Create (form)
  - Read (list + detail)
  - Update (edit form)
  - Delete (with confirmation)

**🟥 Task 18: Add API for same CRUD**
- `/api/articles` (list)
- `/api/article/<id>` (detail)
- POST, PUT, DELETE
- Return JSON

**🟥 Task 19: Connect HTML + API**
- HTML page loads data from API (`fetch`)
- HTML form sends POST to API

**🟥 Task 20: User authentication**
- Login
- Registration
- Restrict article editing to logged-in users

---

### 🔥 ETAP 6 — Final Project (Django 0→Pro)
**🟦 Task 21: Mini blog**
- Users
- Articles
- Comments
- Admin panel
- API
- HTML
- Authentication

This is the level where the project looks like a real commercial application.

---

### 📌 Notes
- Each task can be committed separately to track learning progress.
- You can adjust or extend this roadmap anytime as you learn new concepts.

