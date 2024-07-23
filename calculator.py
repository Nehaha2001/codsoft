num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("choose an operation: ")
operation = input("(+,-,*,/):")
print("1. Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
if operation == "+" :
    result=num1+num2
    print(result)
elif operation == "-" :
    result=num1-num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
     result = num1 / num2
     print(result)
else:
    print("Invalid operator")



