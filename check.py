from storage import load_checkin_data,CSV_CHECKOUT_REGISTER_LOCATION,check_csv_rows,load_books_from_csv,CSV_BOOK_LOCATION
from classes import CheckOut
import csv


class CheckInOutManagement:
    def __init__(self):
        self.checkout = load_checkin_data()

    # User could borrow books by checking out
    def checkoutBook(self, userID,ISBN):
        ch = CheckOut(userID, ISBN)
        self.checkout.append(ch)
        self.decrement_quantity(CSV_BOOK_LOCATION,ISBN)
        self.add_checkoutLog(userID,ISBN)

        return f"Book '{ISBN}' checked out successfully."
    
    # User could return books by checking in 
    def checkInBook(self,userID,ISBN):
        self.increment_quantity(CSV_BOOK_LOCATION,ISBN)

        return f"Book '{ISBN}' checked in successfully."

    # Decrements the quantity of books borrowed when user checks out
    def decrement_quantity(self,file_path, isbn):
        # Reads the CSV file
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames

        # Checks if the 'isbn' and 'quantity' columns exist in the CSV
        if 'ISBN' not in fieldnames or 'QUANTITY' not in fieldnames:
            raise ValueError("Specified columns do not exist in the CSV file")

        # Updates the quantity for the specified ISBN
        updated = False
        for row in rows:
            if row['ISBN'] == isbn:
                row['QUANTITY'] = int(row['QUANTITY'])-1
                updated = True
                break

        if not updated:
            raise ValueError(f"No book with ISBN {isbn} found in the CSV file.")

        # Writes the updated data back to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    # Increments the quantity of books returned when user checks in
    def increment_quantity(self,file_path, isbn):
        # Reads the CSV file
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames

        # Checks if the 'isbn' and 'quantity' columns exist in the CSV
        if 'ISBN' not in fieldnames or 'QUANTITY' not in fieldnames:
            raise ValueError("Specified columns do not exist in the CSV file")

        # Updates the quantity for the specified ISBN
        updated = False
        for row in rows:
            if row['ISBN'] == isbn:
                row['QUANTITY'] = int(row['QUANTITY'])+1
                updated = True
                break

        if not updated:
            raise ValueError(f"No book with ISBN {isbn} found in the CSV file.")

        # Writes the updated data back to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    # Adds the check out list to csv file
    def add_checkoutLog(self,userID,ISBN):
        with open(CSV_CHECKOUT_REGISTER_LOCATION, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if(check_csv_rows(CSV_CHECKOUT_REGISTER_LOCATION)==0):
                writer.writerow(['USERID', 'ISBN'])
            writer.writerow([userID, ISBN])

    # Search Book by ISBN
    def find_book_by_isbn(self, isbn):
        self.books = load_books_from_csv()
        for book in self.books:
            if book.isbn == isbn:
                return book
        return "Book not found."
