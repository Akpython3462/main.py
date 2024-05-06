# Book Review System API

This project implements a RESTful API for a hypothetical book review system using FastAPI.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation
Clone the repository:
git clone https://github.com/Akpyhton3462/book-review-system.git

Running the Application
Navigate to the project directory:
cd book-review-system

Run the FastAPI application:
uvicorn main:app --reload
This will start the FastAPI application, and you can access it at http://localhost:8000.

API Documentation
The API documentation is available at http://localhost:8000/docs. You can use the Swagger UI to interactively test the endpoints.

Directory Structure

book-review-system/
│
├── main.py             # FastAPI application
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies

Endpoints
POST /books: Add a new book (title, author, publication year).
POST /books/{book_id}/reviews: Submit a review for a book (text review, rating).
GET /books: Retrieve all books with an option to filter by author or publication year.
GET /books/{book_id}/reviews: Retrieve all reviews for a specific book.

Technologies Used
FastAPI: Web framework for building APIs with Python
Pydantic: Data validation library
Uvicorn: ASGI server for running FastAPI applications

Authors
Akash Nayak

License
This project is licensed under the MIT License.
