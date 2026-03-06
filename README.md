# django-auth
let's see your id!

Todo API — Django REST Backend

Overview

Todo API is a backend service that allows users to create, manage, and track their personal tasks (todos).
The application exposes a RESTful API where authenticated users can perform CRUD operations (Create, Read, Update, Delete) on their own todos.

Each user has a private workspace. A user must register and log in before accessing or modifying their tasks.

The project is designed as a learning and practical backend project focused on building production-style APIs using Django and Django REST Framework.

---

Features

Authentication

- User registration
- User login
- Token-based authentication
- Protected API routes

Todo Management

Authenticated users can:

- Create new todos
- View their todos
- Update existing todos
- Mark todos as completed
- Delete todos

Each todo belongs to a specific user, and users cannot access other users' data.

Security

- Authenticated access using tokens
- User-specific data filtering
- Ownership validation when updating or deleting tasks

---

Tech Stack

Backend Framework

- Python
- Django

API Framework

- Django REST Framework (DRF)

Database

- SQLite (development)
- PostgreSQL (production ready)

Authentication

- Token-based authentication using DRF

Deployment

- Designed to run on cloud platforms such as Render

Version Control

- Git
- GitHub

---

Project Structure

Typical structure of the project:

todo_api/
│
├── todo/                 # Main application
│   ├── models.py         # Todo model
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   ├── urls.py           # App routes
│
├── todo_api/
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│
├── manage.py
├── requirements.txt
└── README.md

---

API Endpoints

Authentication

Register user

POST /api/register/

Login user

POST /api/login/

Returns authentication token.

---

Todos

Get all todos

GET /api/todos/

Create todo

POST /api/todos/

Update todo

PUT /api/todos/<id>/

Delete todo

DELETE /api/todos/<id>/

All routes require authentication.

---

Installation and Local Setup

1. Clone the Repository

git clone https://github.com/Houzsaad/todo-api.git
cd todo-api

---

2. Create Virtual Environment

python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

---

3. Install Dependencies

pip install -r requirements.txt

---

4. Apply Migrations

python manage.py migrate

---

5. Create Superuser (Optional)

python manage.py createsuperuser

---

6. Run Development Server

python manage.py runserver

Server will run at:

http://127.0.0.1:8000

---

Testing the API

You can test the API using:

- Postman
- cURL
- Insomnia
- DRF Browsable API

Make sure to include the authentication token in the request header:

Authorization: Token <your_token>

---

Future Improvements

Possible upgrades for the project:

- JWT authentication
- Pagination
- Filtering and search
- Task categories
- Due dates and reminders
- Background notifications
- Frontend integration (React or mobile app)

---

Learning Goals of This Project

This project demonstrates practical backend development concepts such as:

- REST API design
- Authentication and authorization
- Database modeling
- Serializer-based data validation
- User-specific data protection
- Deployment-ready backend architecture

---

Author

Backend project developed by Huzaifa Sa'ad (Houzsaad), as part of a backend engineering learning roadmap focused on Django and Django REST Framework.

