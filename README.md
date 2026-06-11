# Student Management System

## Overview

A console-based Student Management System developed using Python and MySQL. This application allows users to perform CRUD (Create, Read, Update, Delete) operations on student records through a menu-driven interface.

## Features

* Add new student records
* View all student records
* Search students by ID
* Update student information
* Delete student records
* MySQL database integration
* Menu-driven console interface

## Technologies Used

* Python
* MySQL
* mysql-connector-python

## Database Setup

Create a database named `student_db` and run the following SQL commands:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);
```

## How to Run

```bash
python student_management.py
```

## Menu Options

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

## Project Structure

```text
student-management-system/
│
├── student_management.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Learning Outcomes

This project demonstrates:

* Python Programming
* MySQL Database Connectivity
* CRUD Operations
* SQL Queries
* Functions and Modular Programming
* Menu-Driven Applications

## Future Enhancements

* Admin Login System
* Search by Name
* Attendance Management
* Student Marks Management
* Export Records to CSV
* Flask-Based Web Interface

## Author

Anshika Dwivedi
B.Tech – Artificial Intelligence and Machine Learning (AIML)
