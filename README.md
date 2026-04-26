# 🧑‍⚖️ Criminal Record Management System (Python)

## 📌 Overview

This project is a **menu-driven Criminal Record Management System** built using Python and Object-Oriented Programming (OOP). It allows users to manage criminal records by performing basic operations such as adding, viewing, and searching records.


## 🏗️ Project Design

The system is based on a class named `Criminal`, which stores all records using Python lists.

### 🔹 Class: `Criminal`

This class is responsible for storing and managing criminal data.

#### Attributes:

* `self.id` → stores criminal IDs
* `self.name` → stores names of criminals
* `self.crime` → stores crime details
* `self.punish` → stores punishment duration (in years)

Each index represents one complete record. For example:

ID[0], Name[0], Crime[0], Punish[0] → One criminal record

## ⚙️ Methods Explanation

### ✅ 1. `add(id, name, crime, punish)`

* Adds a new criminal record into the system
* Stores data in lists using `.append()`

📌 Example:

```python
c1.add(101, "Ali", "Theft", "2 years")

### ✅ 2. `display()`

* Displays all stored criminal records
* If no data exists → prints `"Criminal Record empty"`
* Otherwise → loops through all records and prints them

📌 Uses:

* `for` loop
* `len()` function

### ✅ 3. `search(id)`

* Searches for a criminal using their ID
* If found → prints full details
* If not found → prints `"No record found"`

📌 Logic:

* Loop through all IDs
* Compare input ID with stored IDs
* Use a `found` flag to track result

## 🔁 Main Program Flow

The program runs using an infinite loop:

python
while True:
A menu is displayed to the user:

1. Add record
2. View record
3. Search record
4. Exit

## 🧭 User Choices

### 🔹 Option 1: Add Record

* User inputs:

  * ID
  * Name
  * Crime
  * Punishment
* Data is stored using `add()` method

### 🔹 Option 2: View Records

* Calls `display()` method
* Shows all saved records

### 🔹 Option 3: Search Record

* User enters ID
* Calls `search()` method
* Displays matching record if found


### 🔹 Option 4: Exit

* Terminates the program using `break`

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* Classes and Objects
* Lists for data storage
* Loops (`while`, `for`)
* Conditional statements (`if-else`)
* User input handling

## ▶️ How to Run the Program

1. Open the Python file in any IDE (VS Code, PyCharm, etc.)
2. Run the program:

   python filename.py

3. Follow the menu instructions

If you want, I can next help you turn this into a **professional-level project (with file saving + GUI)** which is much stronger for GitHub and internships.
