import book
import user
import check

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Add User")
    print("6. List User")
    print("7. Update User")
    print("8. Delete User")
    print("9. Search By Title")
    print("10. Search By ISBN")
    print("11. Check Book Availability")
    print("12. Check Out Book")
    print("13. Check In Book")
    print("14. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:

        choice = main_menu()
        book_management=book.BookManagement()
        user_management=user.UserManagement()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            quantity=int(input("Enter Quantity: "))
            book_management.add_book(title, author, isbn,quantity)
            print("Book added.")

        elif choice == '2':
            book_management.list_books()
            print("List of Books.")
        elif choice == '3':
            isbn = input("Enter ISBN: ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_quantity=int(input("Enter Quantity: "))
            book_management.update_book(isbn, new_title, new_author, new_quantity)
            print("Book updated.")

        elif choice == '4':
            title = input("Enter title: ")
            isbn = input("Enter ISBN: ")
            book_management.delete_book(isbn,title)
            print("Book deleted.")

        elif choice == '5':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.add_user(name, user_id)
            print("User added.")

        elif choice == '6':
            user_management.list_users()
            print("List of Users.")

        elif choice == '7':
            user_ID = input("Enter user ID: ")
            old_user_name = input("Enter old  user name: ")
            new_name = input("Enter new user name: ")
            user_management.update_user(user_ID,old_user_name,new_name)
            print("User updated.")

        elif choice == '8':
            user_ID = input("Enter user ID: ")
            name = input("Enter user name: ")
            item = input("Do you want to delete: Yes: Y, No: N ")
            if(item=='Y'):
                user_management.delete_user(user_ID,name)
                print("User deleted.")
            else:
                print("User not deleted.")

        elif choice=='9':
            title=input("Enter Title: ")
            book_management.search_books_by_title(title)

        elif choice=='10':
            isbn=input("Enter ISBN: ")
            books=book_management.search_books_by_isbn(isbn)
            idx=1
            for book_available in books:
                if(idx==1):
                    print('Index','Title', 'Quantity')
                print(idx,' ',book_available.title,' ',book_available.quantity)
                idx+=1

        elif choice=='11':
            isbn=input("Enter ISBN: ")
            book_management.book_availability(isbn)
        
        elif choice=='12':
            isbn=input("Enter ISBN: ")
            userID=input("Enter UserID: ")
            checkout=check.CheckInOutManagement()
            if(book_management.book_availability(isbn)):
                print(checkout.checkoutBook(userID,isbn))

        elif choice=='13':
            isbn=input("Enter ISBN: ")
            userID=input("Enter UserID: ")
            checkin=check.CheckInOutManagement()
            print(checkin.checkInBook(userID,isbn))

        elif choice == '14':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
