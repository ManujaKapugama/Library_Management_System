# 📚 Library Management System
A desktop-based Library Management System developed using Python and CustomTkinter. The application provides a graphical interface for insert books, update book details, delete books & user management

A simple desktop-based **Library Management System** developed using **Python, Tkinter, and SQLite**.

The application is designed to help manage books, members, borrowing, and returning activities in a small library.

## 🚀 Features

* 📖 Add, update, delete, and view books
* 👤 Manage library members
* 🔍 Search for books
* 📚 View available books
* 📤 Issue/borrow books
* 📥 Return books
* 📋 Track borrowing records
* 💾 Store data using SQLite database
* 🖥️ User-friendly desktop interface using Tkinter

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
├── database.py
├── books.py
├── members.py
├── transactions.py
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
* ISBN
* Category
* Quantity
* Available Quantity

### Members

Stores information about library members.

* Member ID
* Name
* Email
* Phone
* Address

### Borrowing / Transactions

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

The application provides a graphical interface where users can manage library books, members, and borrowing transactions.

## 📌 Future Enhancements

* 🔐 User login and authentication
* 👥 Different user roles such as Admin and Librarian
* 📊 Dashboard with library statistics
* 🔔 Overdue book notifications
* 💰 Fine calculation
* 📄 Generate reports
* 🔎 Advanced book search and filtering
* 📤 Export reports to CSV/PDF
* 🌙 Dark mode

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Create a Pull Request

## 📄 License

This project is created for educational and learning purposes.

## 👨‍💻 Author

**Your Name**

---

⭐ If you find this project useful, consider giving the repository a star!



👩‍💻 Developed By

Manuja Kapugama

Final Project – Advanced Python Certification Course at SLIPD
