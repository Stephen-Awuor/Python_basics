weight = float(input("Enter your weight: "))
Unit = input("Kilograms or Pounds? (K or L): ")

if Unit == "K":
    weight = weight * 2.205
    print(f"Your weight is {round(weight, 1)} Pounds")
elif Unit == "L":
    weight = weight / 2.205
    print(f"Your weight is {round(weight, 1)} Kgs")
else:
    print(f"Invalid unit!")
