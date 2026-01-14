# Employee Management REST API

## Project Overview
This project is a RESTful API built using Django and Django REST Framework to manage employee records in a company.  
It provides secure CRUD operations (Create, Read, Update, Delete) on employee data using JWT-based authentication.

This project was developed as part of a Python Backend Developer technical assignment.

---

## Live Demo
Base URL:
https://employee-management-f4y3.onrender.com

---

## Test Credentials (For Evaluation)

Use the following credentials to authenticate and test the secured APIs:

Username: admin  
Password: admin123

---

## Technology Stack
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (Local Database)
- Render (Deployment)

---

## API Summary

- POST /api/token/
- body {
  "username": "admin",
  "password": "admin123"
}

  Generates JWT access and refresh tokens.

- POST /api/token/refresh/  
  Refreshes the JWT access token.

- POST /api/employees/  
  Creates a new employee record.

- GET /api/employees/  
  Lists all employees with pagination and filtering support.

- GET /api/employees/{id}/  
  Retrieves a single employee by ID.

- PUT /api/employees/{id}/  
  Updates an existing employee’s details.

- DELETE /api/employees/{id}/  
  Deletes an employee record.

---
## Postman Testing Note

The Postman collection is named “Employee_API_Postman Collection” and is included in this repository.
Please use this collection to test all secured endpoints.

## Authentication
All employee-related endpoints are secured using JWT authentication.

Add the following header to every request:

Authorization: Bearer <access_token>

---

## Local Setup Instructions

1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd employee-api

2. Create a virtual environment
python -m venv venv

Activate the environment:
Windows: venv\Scripts\activate  
Linux/macOS: source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Run the development server
python manage.py runserver

The server will start at:
http://127.0.0.1:8000/

---

## Notes
- RESTful principles followed
- Proper HTTP status codes implemented
- JWT-based secure authentication
- Filtering and pagination supported
- Designed for interview presentation and live demo

---

Author: Vivek N hebbar
