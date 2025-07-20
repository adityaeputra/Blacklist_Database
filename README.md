# Blacklist Database Management System

A simple command-line Python application for managing a blacklist database of suspicious accounts.  
This system was built without any external libraries (except for `tabulate` for formatting), and serves as a basic CRUD program tailored for anti-fraud use cases.

---

## 🧩 Features

- View the blacklist database in table format
- Add new blacklisted accounts
- Update specific account data (name, phone number, reason, or block status)
- Delete accounts by user ID
- Search for an account by user ID

---

## 📁 Data Structure

Data is stored in a dictionary of lists, representing columns in the blacklist database. Each account consists of the following fields:

| Field        | Description                        |
|--------------|------------------------------------|
| `user_id`    | Unique identifier (int)            |
| `name`       | Account name (str)          |
| `phone`      | Phone number (int, starts with 62) |
| `reason`     | Reason for blacklisting (str)      |
| `is_blocked` | Boolean: `True` if account is blocked |

Example:

```python
blacklist_database = {
    'user_id': [1, 2],
    'name': ['Agus', 'Budi'],
    'phone': [6281234567891, 6281234567892],
    'reason': ['Rule 1', 'Rule 2'],
    'is_blocked': [True, True]
}
