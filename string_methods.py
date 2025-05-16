#length = input("Enter your name: ")

#result=len(length) #len function shows length of a string

#result=length.find("a") #finds the index of a character
#result=length.upper() #makes everything uppercase
#result=length.lower() #makes everything lowercase
#result=length.isdigit() #returns True or False, length.isalpha returns the opposite, length.replace("","") replaces a a value with the other specified value


#print(result)

name = input("Enter your username: ")
if len(name)>=8:
    print("Good enough!")
else:
    print("The username is invalid!")

    #1:44:0