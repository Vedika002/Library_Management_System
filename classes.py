class Book:
    def __init__(self, title, author, isbn,quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity=quantity

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}',quantity='{self.quantity})"


class User:
    def __init__(self, userID, username):
        self.userID = userID
        self.username = username

    def __repr__(self):
        return f"User(userID='{self.userID}', username='{self.username}')"


class CheckOut:
    def __init__(self,userID,ISBN):
        self.userID=userID
        self.ISBN=ISBN
    
    def __repr__(self):
        return f"CheckOut(userID='{self.userID}',username='{self.ISBN}')"