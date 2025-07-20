# Blacklist Database Management System

A simple command-line Python application for managing a blacklist database of suspicious accounts.  
This system was built without any external libraries (except for `tabulate` for formatting), and serves as a basic CRUD program tailored for anti-fraud use cases.

`Please take notes: This app runs using Bahasa Indonesia`

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
```
---

## 🧩 Features

1. View the blacklist database in table format
2. Add new blacklisted accounts
3. Update existing account data (name, phone, reason, is_blocked)
4. Delete accounts from blacklist by user ID
5. Search existing account by user ID
6. Exit Program

Here's the screenshot of the main menu:

<img width="818" height="123" alt="image" src="https://github.com/user-attachments/assets/ebcd186e-f06b-43e0-8397-3e2bfd0b3a8a" />


### **1. View the blacklist database**
Displays all currently blacklisted accounts in a formatted table, showing user ID, name, phone number, reason for blacklisting, and block status.

<img width="818" height="230" alt="image" src="https://github.com/user-attachments/assets/bef9c8ff-2dfe-40a5-8fce-4d4430bbfc13" />

### **2. Add New Blacklisted Account**  
Allows the user to input new account data, including a unique user ID, name, phone number, reason for blacklisting, and block status.

<img width="818" height="431" alt="image" src="https://github.com/user-attachments/assets/2f334a12-ba6e-45b2-a750-d27da74675cc" />

### **3. Update Existing Account Data**  
Enables editing of existing account information based on user ID. Users can update the name, phone number, reason, or the block status.

<img width="818" height="431" alt="image" src="https://github.com/user-attachments/assets/d091ad7e-02bb-4a02-8e47-9e146f0321cc" />

### **4. Delete Account from Blacklist**  
Permanently removes an account from the blacklist database using the user ID as a reference.

<img width="818" height="351" alt="image" src="https://github.com/user-attachments/assets/a9fee73f-07d8-410f-84e9-85deb331c1a0" />

### **5. Search Account by User ID**  
Lets the user search for and display a specific account's details by entering its unique user ID.

<img width="818" height="248" alt="image" src="https://github.com/user-attachments/assets/c3941838-1004-436a-b82e-471f80803f92" />

### **6. Exit Program**  
Closes the program with a confirmation message.

<img width="818" height="131" alt="image" src="https://github.com/user-attachments/assets/69aeccfc-e560-45b4-b738-01dbac5f0597" />

---

This app is created by Aditya Eka Putra / [@adityaeputra](https://github.com/adityaeputra).  
You can reach me through GitHub, LinkedIn, or other social platforms.

