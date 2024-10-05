import re

while True:
    password = input("enter your password: ")
    if (len(password) >= 8 and 
    re.search(r'[A-Z]', password) and 
    re.search(r'[a-z]', password) and
    re.search(r'\d', password)    and      
    (r'[!@#$%^&*(),.?":{}|<>]', password) ):
        print ("your password is valid:")
        break
    else:
        print ("please try again:")
    


