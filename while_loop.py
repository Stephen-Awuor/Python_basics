#while loop  - executes some code while some condition remain true. Useful for verifying user input

password =input("Enter your password: ")
while len(password)<8:
    print("Your password is invalid, Please try again!")
    password =input("Enter your password: ")
print(f"Log in successful!")

#1:58:00
