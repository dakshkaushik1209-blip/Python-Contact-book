# Contact Book (Python)

A simple command-line Contact Book application built using Python. This project allows users to manage contacts with persistent storage using a JSON file.

## Features

*  Add new contacts
*  View all saved contacts
*  Search contacts by name
*  Update contact details

  * Update name
  * Update phone number
  * Update email address
*  Delete contacts
*  View total number of contacts
*  Automatic data saving using `database.json`

##  Technologies Used

* Python
* JSON
* `pathlib`

##  Project Structure

```
Contact-Book/
│── Contact_Book.py
│── database.json
│── README.md
```

##  How to Run

1. Clone this repository:

```bash
[git clone https://github.com/dakshkaushik1209-blip/Contact-Book.git](https://github.com/dakshkaushik1209-blip/Python-Contact-book.git)
```

2. Open the project folder.

3. Run the program:

```bash
python Contact Book.py
```

##  Menu Options

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Statistics
7. Exit
```

##  Input Validation

* Name cannot be empty.
* Phone number must contain only digits.
* Phone number must be exactly 10 digits.
* Duplicate phone numbers are not allowed.
* Duplicate email addresses are not allowed.
* Email must contain `@gmail.com`.

##  Sample Output

```
Welcome to Contact Book

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Statistics
7. Exit
```

##  Future Improvements

* Search by phone number
* Search by email
* Better email validation
* Contact sorting (A–Z)
* Import/Export contacts
* Favorite contacts
* Multiple email domain support

##  What I Learned

* Working with JSON files
* File handling in Python
* Dictionaries and lists
* Functions
* Loops and conditions
* Input validation
* CRUD (Create, Read, Update, Delete) operations

---

 If you found this project helpful, consider giving it a star!

 # Author
 Daksh kaushik  
 B.Tech CSE(AI/ML)  
 First year
