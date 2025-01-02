# #print(5+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15//6)
# print(5%3)
# print(2**4)

print("Welcome to the calculator, Please enter the 2 digit number to perform the operation")
num1 = float(input("\n Enter the first number: "))
num2 = float(input("\n Enter the second number: "))
operation = input("\n Enter the operation you want to perform (+, -, *, / , // , ** , %): ")

if operation == "+":
    print(f"\n {num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"\n {num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"\n {num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f"\n {num1} / {num2} = {num1 / num2}")
elif operation == "//":
    print(f"\n {num1} // {num2} = {num1 // num2}")
elif operation == "**":
    print(f"\n {num1} ** {num2} = {num1 ** num2}")
elif operation == "%":
    print(f"\n {num1} % {num2} = {num1 % num2}")
else:
    print("\n Invalid operation, Please enter the valid operation")
    