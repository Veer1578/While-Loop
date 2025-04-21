num1 = float(input("Enter a number "))
num2 = float(input("Enter another number "))

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1
print(f"Hcf of value 1 and value 2 is {hcf}")
