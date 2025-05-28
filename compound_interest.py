import math
p=0
r=0
t=0

while p <=0:
    p=float(input("Enter the principle amount: "))
    if p<=0:
        print("Principle can't be less than or equal to zero!")

while r <= 0:
    r = float(input("Enter the interest rate: "))
    if r <= 0:
        print("rate can't be less than or equal to zero!")

while t <= 0:
    t = int(input("Enter the period in years: "))
    if t <= 0:
        print("Period can't be less than or equal to zero!")

CI=p * pow((1 + r / 100),t)
print(f"Your total amount will be ${CI: .2f} after {t} years: ")





