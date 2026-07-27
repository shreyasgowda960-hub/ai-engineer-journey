u_name=input("Enter your Username: ")

password=input("enter password: ")

if u_name!="admin":
    print("User not found")
elif password!="1234":
    print("Wrong password")
else:
    print("login successful")        

