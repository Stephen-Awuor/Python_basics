# input() - prompts the user to enter input
from Variables import quantity

name = input("What is your name?:")
#print("Hello ", name) #Another method
age = input("How old are you?:")
print(f"Hello {name}")
print(f"You are {age} years old!")
#the two give same result

#Calculate the area of a rectangle
print("Let's do some Math")
length =float(input("Enter the length of the rectangle:")) #You have to typecast as either float or int(Using float will accomodate both)
width = float(input("Enter the width of the rectangle:"))
area = length * width
print(f"The area of the rectangle is {area} cm")


