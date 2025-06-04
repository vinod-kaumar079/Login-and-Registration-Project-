# Flask Login & Registration Project

A simple, secure, and user-friendly **Login and Registration system** built with **Flask** and **MySQL**. This project demonstrates basic user authentication, session management, and form validation using Python and Flask.

---

## Features

- User registration with username, email, and password.
- Form validation with email and username format checks.
- Secure login with session handling.
- User logout functionality.
- Password storage (currently plain text, consider hashing for production).
- Clean and modern UI with responsive design.
- Modular code with separate routes and database connection handling.

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS (with responsive & modern UI)
- **Other:** Regular Expressions (for validation), Flask Sessions

---

## Prerequisites

- Python 3.7+
- MySQL Server installed and running
- pip (Python package installer)

---

## Setup Instructions

1. Clone the repository

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name


2. Create and activate virtual environment

    python -m venv env
    # Windows
    .\env\Scripts\activate
    # Linux / Mac
    source env/bin/activate

3. Install dependencies

    pip install -r requirements.txt

4. Setup MySQL Database

    Login to MySQL and create the database and table:

        CREATE DATABASE login;

        USE login;

        CREATE TABLE accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        );

5. Configure your MySQL credentials

    Open app.py and update the MySQL connection details (host, user, passwd) if needed.

6. Run the Flask application
    
    .in terminal 
    . python app.py --> for bash

7. Access the app
    Open your browser and go to: http://127.0.0.1:5000/login

Folder Structure

    ├── app.py
    ├── templates/
    │   ├── index.html
    │   ├── login.html
    │   ├── register.html
    ├── static/
    │   ├── style.css
    ├── requirements.txt
    └── README.md

Notes & Improvements
    Security: Currently, passwords are stored in plain text — use password hashing (e.g., bcrypt) for production.

    Validation: Enhance validation for stronger password rules.

    Error Handling: Add more robust error handling and user feedback.

    Features: Add email verification, password reset, and OAuth login.


Author
    Vinod Kumar Prajapat

    GitHub: https://github.com/kaumar-vinod079

    LinkedIn: --