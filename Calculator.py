operation = input("What operation would you like to perform (+,-,*,/)?")

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
result = 0

if operation.upper() == "+":
	result = num1 + num2
elif operation.upper() == "-":
	result = num1 - num2
elif operation.upper() == "*":
	result = num1 * num2
elif operation.upper() == "/":
	result = num1 / num2

print(str(num1) + operation + str(num2) + " = " + str(result))


#