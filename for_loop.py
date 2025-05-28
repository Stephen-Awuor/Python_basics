#for loop - executes a block of code a fixed number of times

for x in range(1,10):
    print(x, end=" ")

#while loop - repeats a block of a code while so long as a conditions remains true
count = 0
while count < 5:
    print("Hello!")
    count += 1
#this prints 4 hellos because it stops as soon as it's equal or more than 5
#nested loop is a loop within another loop
for y in range (3):
  for x in range(1,10):
    print(x, end=" ")
    print(y)

