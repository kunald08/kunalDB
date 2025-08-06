
## 📸 First take a look at demo then read the README

> 📦![Demo GIF](./assets/demo.gif)

# 🗃️ KunalDB

**kunalDB** is a simple, interactive, file-based database management system written in Python. It allows you to create, edit, delete, import, export, and visualize tabular data using a custom `.kunal` file format. The tool is designed for learning and small-scale data management tasks, with a command-line interface and basic features similar to a spreadsheet or CSV editor.

---

## 🚀 Features

- **Add, Edit, Delete Records:** Manage your data records interactively.
- **Custom Table Structure:** Define your own fields/columns.
- **Import/Export:**  
  - Import data from CSV files.  
  - Export data to CSV or HTML for use in Excel or web pages.
- **Table Visualization:** Display data as formatted tables in the terminal.
- **Search:** Find records using regular expressions.
- **Plot Graphs:** Simple ASCII bar graphs for numeric data.
- **Multiple Databases:** Switch between different `.kunal` files.
- **File Overwrite Protection:** Prevent accidental data loss with overwrite confirmations.

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kunald08/KunalDB.git
cd KunalDB
```

### 2. Install dependencies

Only one optional dependency for colored output:

```bash
pip install colorama
```

> App works without `colorama`, but terminal output won't be colored.

### 3. Run the script

```bash
python kunalDB.py
```

---

## 📌 Menu Options

```
Make a selection: 

1) Add a record
2) Delete a record
3) Edit a record
4) Overwrite the file
5) Display as table
6) Display as csv
7) Plot a Graph (BETA)
8) Find in table
9) Import CSV
10) Export As...
11) Switch DB
12) EXIT
```

---

## 📂 File Format

- Data is stored in binary `.kunal` files using Python's `pickle` module.
- Each file contains a table structure (field names) and records.

---

## 🧠 Behind the Scenes

- Pure Python (no SQL used)
- Uses OOP (`dataClass`) for record encapsulation
- Highlights matching records using terminal styling
- ASCII graph plotting with scaling

---

## Notes

- This project is for educational and small-scale use only.
- `.kunal` files are not compatible with other database systems.
- Always back up your data before overwriting files.


## 🧑‍💻 Author
[Kunal Dharpure](https://x.com/kunald08_) <br>
Made with ❤️ for CLI nerds


## ⚖️ License

[MIT License](LICENSE) © 2025 Kunal Dharpure

---

