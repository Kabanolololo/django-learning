# 🐍 Django Learning Roadmap — Net Ninja Edition

Welcome to my learning subfolder! 🚀  
This folder contains my learning progress while following the YouTube course from **The Net Ninja**.

---

## 📑 Table of Contents

- [📌 Learning source](#-learning-source)
- [📺 Episode 2 — Setup & Installation (used commands)](#-episode-2--setup--installation-used-commands)
- [📺 Episode 3 — Django Basics](#-episode-3--django-basics)
- [📺 Episode 4 — Database Setup](#-episode-4--database-setup)

## 📌 Learning source

🎥 **Django Tutorial – The Net Ninja**  
👉 https://www.youtube.com/watch?v=aAACOgAHg90&list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw

---

## 📺 Episode 2 — Setup & Installation (used commands)

In this episode I learned how to create a Django project and a Django app, and how to work with a virtual environment using Pipenv.

### 🔧 Commands used in the video

- `pipenv shell`  
  Activates the virtual environment created by Pipenv, so all installed packages and commands are isolated for this project.

- `pipenv install django`  
  Installs Django inside the virtual environment and adds it to the project dependencies.

- `pip freeze`  
  Displays a list of all Python packages installed in the current environment together with their versions.

- `django-admin startproject myproject`  
  Creates a new Django project called **myproject** with the default project structure.

- `python manage.py startapp myapp`  
  Creates a new Django application called **myapp** inside the project.

- `python manage.py runserver`  
  Starts the local development server so the project can be viewed in the browser.

---

## 📺 Episode 3 — Django Basics

In this episode I learned how Django handles requests using views and URL routing.

### 🔧 Things used in the video

- creating a function-based view in `views.py`  
  Defines what should be returned when a user visits a specific page.

- using `HttpResponse`  
  Returns a simple text response from a view.

- connecting a view to a URL in `urls.py`  
  Maps a URL path to a specific view function.

- understanding the URL → view flow  
  Shows how Django decides which view handles a request.

- testing the page in the browser using `runserver`  
  Confirms that the view and URL configuration work correctly.

---

## 📺 Episode 4 — Database & Migrations

In this episode I learned how to work with Django models and how to apply database migrations.

### 🔧 Things used in the video

- `python manage.py makemigrations`  
  Creates migration files based on changes in models.

- `python manage.py migrate`  
  Applies migrations and updates the database structure.

- creating a model in `models.py`  
  Defines database tables using Python classes.

- understanding how Django ORM works  
  Allows working with the database using Python instead of SQL.

- creating and updating the database schema using migrations  
  Keeps the database in sync with the project models.