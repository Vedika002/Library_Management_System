# Library_Management_System

This project is a simple Library Management System implemented in Python. It allows for the management of books and users, tracking of book availability, and simple logging of operations.

## Features

1. **Manage Books**
   - Add new books to the library.
   - Update details of existing books.
   - Delete books from the library.
   - List all books in the library.
   - Search for books by various attributes like title, author, or ISBN.

2. **Manage Users**
   - Add new users to the system.
   - Update user information.
   - Delete users from the system.
   - List all users in the system.
   - Search for users by attributes like name or user ID.

3. **Check Out and Check-In Books**
   - Users can check out books from the library.
   - Users can check in books back to the library.
   - Track the due dates for borrowed books.

4. **Track Book Availability**
   - Keep track of which books are currently available.
   - See which books are checked out and by which users.

5. **Simple Logging of Operations**
   - Log operations like adding, updating, deleting books and users, and checking out and checking in books.

## Project Structure

The project consists of the following files:

- `user.py`: Contains user-related functionalities.
- `book.py`: Contains book-related functionalities.
- `transaction.py`: Contains functionalities for checking out and checking in books.
- `storage.py`: Contains functions to save and update data in CSV files.
- `log.py`: Contains functions for logging operations.
- `CSV_USER_LOCATION.csv`: The CSV file where user data is stored.
- `CSV_BOOK_LOCATION.csv`: The CSV file where book data is stored.

## Installation
1. Clone the repository :
   git clone https://github.com/username/Library_Management_System.git
2. Navigate to the project directory:
   cd Library_Management_System
3. Run the main script (if available) to start the application.
