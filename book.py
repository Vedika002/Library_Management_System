from storage import load_books_from_csv, save_book_to_csv, update_books_to_csv, delete_book_from_csv
from classes import Book
from fuzzywuzzy import fuzz


class BookManagement:
    def __init__(self):
        self.books = load_books_from_csv()
    #Adds book details 
    def add_book(self, title, author, isbn,quantity):
        new_book = Book(title, author, isbn,quantity)
        self.books.append(new_book)
        save_book_to_csv(new_book,quantity)
        return f"Book '{title}' added successfully."
    
    # Updates books details
    def update_book(self, isbn, new_title, new_author, new_quantity):
        
        for book in self.books:
            if book.isbn == isbn:
                
                new_book=Book(new_title, new_author, isbn, new_quantity)
                update_books_to_csv(new_book,new_quantity)   
                return f"Book with ISBN '{isbn}' updated successfully."
        return f"Book with ISBN '{isbn}' not found."
    
    # Delete Book details
    def delete_book(self, isbn, title):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                delete_book_from_csv(book)
                return f"Book with ISBN '{isbn}''{title}' deleted successfully."
        return f"Book with ISBN '{isbn}' not found."
    
    # List of books available in Library
    def list_books(self):
        self.books = load_books_from_csv()  # Reload books from the CSV file each time list_books is called
        for index,book in enumerate(self.books):
            print(index+1,book.title)
        return self.books
    
    # Search book by isbn
    def find_book_by_isbn(self, isbn):
        self.books = load_books_from_csv()  # Ensure the books list is up to date
        for book in self.books:
            if book.isbn == isbn:
                return book
        return "Book not found."
    
    # Search books by title
    def search_books_by_title(self, title, threshold=50):
        self.books = load_books_from_csv()
        found_books = []
        idx=1
        for book in self.books:
            similarity = fuzz.partial_ratio(title.lower(), book.title.lower())
            if similarity >= threshold:
                if(idx==1):
                    print('Index','Title', 'Quantity')
                found_books.append(book)
                print(idx,' ',book.title,' ',book.quantity)
                idx+=1
        return found_books

    def search_books_by_isbn(self, isbn):
        self.books = load_books_from_csv()
        found_books = []
        for book in self.books:
            if isbn in book.isbn:
                found_books.append(book)
        return found_books
    
    # Check book availability
    def book_availability(self,isbn):
        book_result=self.search_books_by_isbn(isbn)
        if(len(book_result)>0 and int(book_result[0].quantity)>0):
                print("Book is available.")
                return True
        else:
                print("Book is not available.")
                return False

