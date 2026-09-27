# 📚 Library Management System
A desktop-based Library Management System developed using Python, Tkinter & sqlite. The application provides a graphical interface for insert books, update book details, delete books & user management.

A simple desktop-based **Library Management System** developed using **Python, Tkinter, and SQLite**.

## 🚀 Features

* 📖 Add, update, delete, and view books
* 👤 Manage library members - [Pending]
* 🔍 Search for books
* 📚 View available books
* 📤 Issue/borrow books - [Pending]
* 📋 Track borrowing records - [Pending]
* 💾 Store data using SQLite database


## 🛠️ Technologies Used

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Application development  |
| Tkinter    | Graphical User Interface |
| SQLite     | Database management      |

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py
│
├── library.db
│
├── assets/
│   └── Logo.png
│
└── README.md
```

## 🗄️ Database

The application uses **SQLite** as the database.

The main tables are:

### Books

Stores information about library books.

* Book ID
* Title
* Author
* Available Quantity

### Members - [Pending]

Stores information about library members.

* Member ID
* Name
* Email
* Phone
* Address

### Borrowing / Transactions - [Pending]

Stores book borrowing and returning information.

* Transaction ID
* Book ID
* Member ID
* Issue Date
* Return Date
* Status

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd Library-Management-System
```

### 3. Check Python installation

```bash
python --version
```

Python 3.x is recommended.

### 4. Run the application

```bash
python main.py
```

## 🖥️ Application

The application provides a graphical interface where users can manage library books, members, and borrowing transaction


👩‍💻 Developed By

Manuja Kapugama

Final Project – Advanced Python Certification Course at SLIPD
