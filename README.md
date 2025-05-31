
# 🎓 Student Database Management System

A desktop-based GUI application built with **Python** and **Tkinter** for managing student records efficiently. It uses **SQLite** as the database backend and allows users to add, search, update, view, and delete student information.
![image](https://github.com/user-attachments/assets/0c25f6d4-bb40-4774-91b1-8dd635f5b73c)

---

## ✨ Features

- 📋 Add new student records
- 🔍 Search for students using various fields
- 🔁 Update existing student data
- ❌ Delete student records
- 📄 View all stored records in a listbox
- 🧼 Clear form entries
- 💾 Persistent storage with SQLite
- 🎨 Clean, easy-to-use Tkinter interface

---

## 🗃️ Tech Stack

- **Python 3.x**
- **Tkinter** — GUI Framework
- **SQLite3** — Embedded database
- Built-in `tkinter.messagebox` and `Listbox` widgets for UI functionality

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/student-database-management.git
cd student-database-management

# Run the application
python Student_Database_FrontEnd.py
```

---

## 📁 File Structure

```
student-database-management/
├── Student_Database_FrontEnd.py     # Tkinter GUI and event handling
├── stdStudent_BackEnd.py            # Database logic (CRUD operations)
├── Student.db                       # SQLite database file (auto-created)
└── README.md                        # Project documentation
```

---

## 🧪 How It Works

1. The frontend provides fields for student details like ID, name, DoB, age, etc.
2. Actions such as Add, Update, Delete, and Search interact with the SQLite backend.
3. The Listbox displays all the records and updates dynamically.

---

## 📌 Example Fields

- Student ID
- First Name
- Surname
- Date of Birth
- Age
- Gender
- Address
- Mobile Number

---

## ✅ TODO (Suggestions)

- [ ] Add CSV export/import support
- [ ] Enable sorting or filtering features
- [ ] Add date picker for DoB
- [ ] Add login system with user roles

---

## 📃 License

This project is released under the **MIT License**.

---

> Developed with ❤️ using Python and Tkinter
