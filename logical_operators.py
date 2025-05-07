#or - atleast one condition must be true
#and - both conditions must be true
#not - inverts the condition


#temp = float(input("Enter the temperature: "))
#if temp > 25 or temp == 25:
    #print("You can play outside!")
#else:
    #print("To cold to go outside!")

#is_sunny = False
#temp = float(input("Enter the temperature: "))
#if temp >= 25 and is_sunny:
   # print("You can play outside!")
#else:
    #print("To cold to go outside!")

    #Logical expressions - a one line shortcut to logical operators. X if condition, else Y
temp = 20
weather = "HOT" if temp>=25 else "COLD"
print(weather)

user_role = "guest"
access = "Full Access" if user_role == "admin" else "No Access"
print(access)

#1:27:01


