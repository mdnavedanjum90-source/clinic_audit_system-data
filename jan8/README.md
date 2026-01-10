# 🔐 Vault OS – Personal Password Management

The goal of this project is to help **absolute beginners** understand and apply core Python data structures in a real-world inspired scenario.

## 📌 Problem Statement

Write  a Python program that **collects and organizes basic user account data** using:
- Lists  
- Tuples  
- Dictionaries  
- Sets  

The program simulates a simple **password/account manager** by storing usernames, platforms, and account types.


## 🧾 User Input Requirements

The program asks the user to enter:

- **Username**
- **Platform name** (e.g. GitHub, Instagram, Gmail)
- **Account type** (Personal / Work)


## 🗂️ Data Storage Logic

The data is stored as follows:

| Data | Structure Used |
|----|----|
| All usernames | List |
| Platform & account type | Tuple |
| Username → platform mapping | Dictionary |
| Unique account types | Set |

---

## 🧪 Sample Input


Enter username: ali_khan
Enter platform: github
Enter account type: work

---

## 📤 Sample Output


--- ACCOUNT DATA SUMMARY ---
Usernames       : ['ali_khan']
Platform & Type : ('github', 'work')
User Mapping    : {'ali_khan': 'github'}
Account Types  : {'work'}

