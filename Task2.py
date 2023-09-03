def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        print('Cannot divide by 0')
    return x/y
def power(x,y):
    return x**y
def mod(x,y):
    return x%y

def calculator():
  while True:
    print()
    print("Enter which operation you want to perform : ")
    print()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print()
    choice=input("Enter your choice : ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} / {num2} = {div(num1, num2)}")
    elif choice == '5':
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter power number: "))
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} % {num2} = {mod(num1, num2)}")
    elif choice == '7':
        print('Exit application')
        break
    else:
        print("Invalid input")

calculator()