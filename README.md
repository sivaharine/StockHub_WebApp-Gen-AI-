# StockHub_WebApp-Gen-AI-
    🏷️ Project Title: StockHub – Product Management API
📖 Description

StockHub is a FastAPI-based backend application designed to manage product inventory efficiently.
It allows users to perform all CRUD operations — Create, Read, Update, and Delete — on product data using RESTful API endpoints.
The project uses SQLAlchemy as the ORM for seamless database integration and Pydantic for data validation, ensuring clean, structured, and scalable API development.

This project serves as an excellent starting point for building full-stack inventory or e-commerce management systems.

⚙️ Features

🧩 CRUD Operations: Add, view, update, and delete product details

⚡ FastAPI Framework: High-performance Python web framework

🗃️ SQLAlchemy Integration: Simplified and efficient database interaction

🔐 CORS Middleware: Allows connection with any frontend client

🧱 Modular Structure: Clean separation of models, schemas, and database logic

🧰 Tech Stack

Backend: FastAPI

ORM: SQLAlchemy

How to Run

Install Dependencies
pip install fastapi uvicorn sqlalchemy pydantic

 Run the Application
uvicorn api:app --reload

 Access the App

Once the server starts, open your browser and visit:
👉 http://127.0.0.1:8000

You can also view the interactive Swagger UI at:
👉 http://127.0.0.1:8000/docs

Validation: Pydantic

Language: Python 3.11+
