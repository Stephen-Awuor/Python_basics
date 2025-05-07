temperature = float(input("Enter the temperature: "))
unit = input("What is the unit? (F/C): ")

if unit == "F":
    temperature = temperature / 33.8
    print(f"The temperature is {round(temperature, 1)} degrees celcious")
elif unit == "C":
    temperature = temperature * 33.8
    print(f"The temperature is {round(temperature, 1)} Fahrenheit")
else:
    print("Invalid unit")

    #1:14:00