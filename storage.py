import csv
import os
from classes import Book, CheckOut, User

STORAGE_LOCATION='store/'
os.makedirs(STORAGE_LOCATION, exist_ok=True)
CSV_BOOK_FILENAME ='books.csv'
CSV_USER_FILENAME='user.csv'
CSV_CHECKOUT_REGISTER='checkout.csv'
CSV_BOOK_LOCATION=STORAGE_LOCATION+CSV_BOOK_FILENAME
CSV_USER_LOCATION=STORAGE_LOCATION+CSV_USER_FILENAME
CSV_CHECKOUT_REGISTER_LOCATION=STORAGE_LOCATION+CSV_CHECKOUT_REGISTER

def load_books_from_csv():
    books = []
    try:
        with open(CSV_BOOK_LOCATION, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                books.append(Book(row['TITLE'], row['AUTHOR'], row['ISBN'],row['QUANTITY']))
    except FileNotFoundError:
        pass  # If the file doesn't exist, just return an empty list
    return books

def save_book_to_csv(book,quantity):
    with open(CSV_BOOK_LOCATION, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if(check_csv_rows(CSV_BOOK_LOCATION)==0):
            writer.writerow(['TITLE', 'AUTHOR', 'ISBN','QUANTITY'])
        writer.writerow([book.title, book.author, book.isbn,quantity])


def check_csv_rows(csvfile):
    rows = []
    try:
        with open(csvfile, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        return 0
    return len(rows)

def save_user_to_csv(user):
    with open(CSV_USER_LOCATION, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if(check_csv_rows(CSV_USER_LOCATION)==0):
            writer.writerow(['USERID', 'USERNAME'])
            
        writer.writerow([user.userID, user.username])

def load_users_from_csv():
    users = []
    try:
        with open(CSV_USER_LOCATION, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(User(row['USERID'], row['USERNAME']))
    except FileNotFoundError:
        pass  # If the file doesn't exist, just return an empty list
    return users

def update_user_in_csv(new_user,user_ID):
    users=[]
    
    with open(CSV_USER_LOCATION, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        for row in reader:
            if row[0] == user_ID:
                row[1] = new_user.username
            users.append(row)    

    with open(CSV_USER_LOCATION, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(users)

def load_checkin_data(csvfile=CSV_CHECKOUT_REGISTER_LOCATION):
    users = []
    try:
        with open(csvfile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(CheckOut(row['USERID'], row['ISBN']))
    except FileNotFoundError:
        pass  # If the file doesn't exist, empty list is returned
    return users

def update_books_to_csv(new_book,new_quantity):
    books=[]
    with open(CSV_BOOK_LOCATION, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[2] == new_book.isbn:
                row[0] = new_book.title
                row[1] = new_book.author
                row[3] = new_book.quantity
            books.append(row)
    
    with open(CSV_BOOK_LOCATION, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(books)

def delete_user_from_csv(user_delete):
    users = []
    with open(CSV_USER_LOCATION, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[0] != user_delete.userID:
                users.append(row)
    
    with open(CSV_USER_LOCATION, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(users)

def delete_book_from_csv(book_to_delete):
    books = []
    with open(CSV_BOOK_LOCATION, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[2] != book_to_delete.isbn:
                books.append(row)
    
    with open(CSV_BOOK_LOCATION, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(books)

    