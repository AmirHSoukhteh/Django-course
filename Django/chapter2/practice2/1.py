user_name = input("Enter your username: ")
password = input("Enter your password: ")

if user_name == "admin":
    if password == "admin":
        print("successful login")
    else:
        print("incorrect password")
else:
    print("user not found")