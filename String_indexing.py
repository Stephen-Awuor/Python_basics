#sting indexing allows us to access the elements of a sequence. [start:end]

credit_number ="1234-5678-9123-456"
print(credit_number[0])
print(credit_number[0:4]) #prints the first 4 digits of a string

#a program to get the last 4 digits of a credit card number
credit_number ="1234-5678-9123-4567"
last_digits = credit_number[-4:]
print(f"{last_digits}")