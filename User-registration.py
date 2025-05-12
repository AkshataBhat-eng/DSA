
import re
import json
import os
import bcrypt

file_path = 'user_list.json'
user_list = []
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def displayUserInfo(self):
        print("User Information \n")
        print("username:", self.username, "email:", self.email)

    def registerUser(self):
        self.username = input("Enter user name")
        self.email = input("Enter email address")
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r+') as file:
                try:
                    user_list = json.load(file)
                except json.JSONDecodeError:
                    user_list = []
        else:
            user_list = []
        if not valid:
            print("email id is not valid")
            return

        for user in user_list:
            if user["email"] == self.email:
                print("email id already exists") 
                return     
        self.password = input("Enater password")
        salt = bcrypt.gensalt()
        encoded_pass = self.password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_pass, salt)

        user_list.append({
            'username': self.username,
            'email': self.email,
            'password': hashed_password.decode('utf-8')
        })
        with open('user_list.json','w') as file:
            json.dump(user_list, file)
        print("New user created")

user1 = User("akshata", "aks@gmail.com", "secret")
user1.displayUserInfo()
user1.registerUser()
user1.displayAllUser()
