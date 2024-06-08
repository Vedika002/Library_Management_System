# user_management.py
from storage import save_user_to_csv,load_users_from_csv, update_user_in_csv, delete_user_from_csv
from classes import User



class UserManagement:
    def __init__(self):
        self.users = load_users_from_csv()

    # Adds the user details
    def add_user(self, username,userID):
        new_user = User(userID, username)
        self.users.append(new_user)
        save_user_to_csv(new_user)
        return f"User '{username}' added successfully."
    
    # List the user details
    def list_users(self):
        self.users = load_users_from_csv()  # Reloads books from the CSV file each time list_books is called
        for index,user in enumerate(self.users):
            print(index+1,user.username)
        return self.users
    
    # Updates the user details
    def update_user(self,userID,old_user_name,new_name):
        for user in self.users:
            if user.userID == userID:
                new_user = User(userID, new_name)
                # self.users.append(new_user)
                update_user_in_csv(new_user, userID)
                return f"User '{old_user_name}' updated successfully to '{new_name}'."
            
            else :
                return f"User with userID '{userID}' not found."

    #deletes the user details
    def delete_user(self, userID, name):
        for user in self.users:
            if user.userID == userID:
                self.users.remove(user)
                delete_user_from_csv(user)
                return f"User'{name}' deleted successfully."
        return f"User with userID '{userID}' not found."    
            
    

        