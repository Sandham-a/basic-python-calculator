# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers and rounds number into something readable
def divide(x, y):
    divide_answer = x/y
    divide_answer = round(divide_answer,2)
    return divide_answer


while True:
    # take input from the user
    try:
        user_choice = input("Enter choice(+,-,*,/): ")
    except ValueError:
        print("Invalid choice please enter one of the options provided")
    # check if choice is one of the four options
    if user_choice in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
# Addition
        if user_choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
            
            with open('equations.txt','a') as answer_file:
                answer_file.write(f"{num1} + {num2} = {add(num1, num2)}\n")  
# Subtraction
        elif user_choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

            with open('equations.txt','a') as answer_file:
                answer_file.write(f"{num1} * {num2} = {subtract(num1, num2)}\n")  
# Multiply
        elif user_choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

            with open('equations.txt','a') as answer_file:
                answer_file.write(f"{num1} * {num2} = {multiply(num1, num2)}\n")  
# Divide
        elif user_choice == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            with open('equations.txt','a') as answer_file:
                answer_file.write(f"{num1}/{num2}={divide(num1, num2)}\n")    
                
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do another calculation? (yes/no): ").lower()
        if next_calculation == "no":
          break
    else:
        print("Please select from +,-,*,/")
try:
    with open('equations.txt', 'r') as answer_file:
        for current_line in answer_file.readlines():
            print(current_line)
except FileNotFoundError as error:
    print("The file not found please have a look")