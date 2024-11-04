#Python program for simple calculator


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


while True:
    print("\nPlease select operation:" 
          "\n1. Add" 
          "\n2. Subtract" 
          "\n3. Multiply" 
          "\n4. Divide")

    
    select = int(input("Select operation from 1, 2, 3, 4: "))

    if select in [1, 2, 3, 4]:
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if select == 1:
            print(f"{number_1} + {number_2} = {add(number_1, number_2)}")

        elif select == 2:
            print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")

        elif select == 3:
            print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")

        elif select == 4:
            print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")

    
        next_calculation = input("Do you want to do another calculation? (yes/no): ").lower()
        if next_calculation == "no":
            break
    else:
        print("Invalid input, please select a valid operation.")