# 🏥 Clinical Audit System (Python)

## 📌 Project Overview

This project is a **Clinical Data Audit System** built using Python.  
It validates patient details, audits heart rate readings, and generates a final audit result using **functions, recursion, and UUID**.
---

## ⚙️ Features

- Takes patient details:
  - Name
  - Age
  - Number of heart rate readings
- Validates input using functions
- Uses **recursion** to collect heart rate readings
- Generates a unique Audit ID using `uuid4()`
- Detects:
  - ❌ Invalid inputs (Flags)
  - ⚠️ High heart rate values (Warnings)
- Produces final audit status:
  - PASS  
  - REVIEW  
  - FAIL  

---

## 🛠️ Technologies Used

- Python 3
- Built-in `uuid` module
- Functions and recursion

---

## 📋 Audit Rules

### Validation Rules
- Age must be between **0 and 120**
- Heart rate must be **numeric**
- Heart rate above **180** generates a warning

### Final Result Logic

| Condition | Status |
|--------|--------|
| Any invalid input | FAIL |
| No flags but warnings | REVIEW |
| No flags and no warnings | PASS |

🧪 Sample Run

Input:

Enter patient name: Ayaan
Enter age: 22
Enter number of readings: 3
78
185
80


Output:

Audit ID : 9c1e4b8e-8c22-4b1a-bd3e-99f22a23e233
Status   : REVIEW
Flags    : None
Warnings : High heart rate detected

📚 Concepts Used

-Functions

-Recursion

-Input validation

-Conditional statements

UUID (uuid4())

Lists

👨‍💻 Author
