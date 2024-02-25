import math

def calculation():
    first_no = int(input("Enter the first number? "))
    second_no = int(input("Enter the second number? "))
    oper = input("Please select the operation (+, -, *, /): ")

    if oper == "+":
        result = first_no + second_no
    elif oper == "-":
        result = first_no - second_no
    elif oper == "*":
        result = first_no * second_no
    elif oper == "/":
        if second_no != 0:
            result = first_no / second_no
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Error: Invalid operation!")
        return

    print("Result:", result)

calculation()
