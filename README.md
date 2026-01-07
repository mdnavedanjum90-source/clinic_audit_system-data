# 🏥 Clinical Data Audit System (Python)

## Python Winter Sprint 2026  
**Core Track – Functions and Recursion**

---

## 📌 Project Description

This project is a **Clinical Data Audit System** written in Python.  
It audits basic patient clinical data using **functions and recursion**, as required in the Python Winter Sprint 2026 assignment.

The system validates patient details, audits heart rate readings, and determines a final audit status based on predefined rules.

Each audit is uniquely identified using Python’s built-in `uuid` module.

---

## 🧠 Features

- Takes patient details:
  - Name
  - Age
  - Number of heart rate readings
- Uses **functions** for validation
- Uses **recursion** to input heart rate readings
- Generates a **unique Audit ID**
- Detects:
  - Invalid inputs (Flags)
  - High heart rate values (Warnings)
- Produces a final audit result:
  - **PASS**
  - **REVIEW**
  - **FAIL**

---

## 🛠️ Technologies Used

- Python 3
- Built-in `uuid` module

---

## 📋 Audit Logic

### Validation Rules

- Age must be between **0 and 120**
- Heart rate must be **numeric**
- Heart rate **greater than 180** triggers a warning

### Final Audit Status

| Condition | Status |
|---------|--------|
| Any invalid input | **FAIL** |
| No flags but warnings | **REVIEW** |
| No flags and no warnings | **PASS** |

---

## ▶️ How the Program Works

1. User enters patient name
2. User enters age
3. User enters number of heart rate readings
4. Heart rate readings are taken **recursively**
5. System validates data
6. Final audit report is displayed

---

## 🧪 Sample Input

