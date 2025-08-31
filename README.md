# 🛎️ Room Service Management System

A Django-based web application designed to streamline room service operations in hospitality environments. It enables staff and guests to manage service requests efficiently with real-time updates and role-based access.

## 🚀 Features

- Secure user authentication and role-based access (Admin, Staff, Guest)
- Dynamic service request creation, tracking, and status updates
- Responsive UI built with Bootstrap for cross-device compatibility
- Real-time interactions using AJAX and Django views
- Scalable architecture with modular codebase and Django ORM

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default), easily switchable to PostgreSQL  
- **Tools:** AJAX, Django Admin, Django ORM

## 📦 Installation

```bash
git clone https://github.com/ak2003335/room_service-using-django.git
cd room_service-using-django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
