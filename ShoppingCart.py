#shopping cart program
item = input("What item would you want to buy?:")
price = float(input("What is the price:?"))
quantity = int(input("How many would you want to buy:?"))

total = price * quantity
print(f"You have bought {quantity} {item} at {price}")
print(f"Your total is: ${total}")