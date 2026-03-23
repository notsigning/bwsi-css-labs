"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
def input_num(prompt: str) -> float:
    """
    Function that takes input until an appropriate number is inputted

    Args: 
        prompt (str): The prompt to the user
    
    Returns:
        float: The inputted number
    """
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please try again.")
def do_calculation(num1: float, num2: float) -> bool:
    """
    Function that inputs an operation until a proper operation is selected

    Args: 
        prompt (str): The prompt to the user
    
    Returns:
        float: The inputted number
    """
    while True:
        try:
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            # Perform the calculation and display the result
            result = simple_calculator(operation, num1, num2)
            print(f"The result of {operation}ing {num1} and {num2} is: {result}")
            return True
        except ValueError:
            print("Something went wrong, please input the right operation.")
        except ZeroDivisionError:
            num2 = input_num("Input a different second value/operation (your inputted values caused a zero division error): ")
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Please select a different operation/second value")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = input_num("Enter the first number: ")
    num2 = input_num("Enter the second number: ")
    do_calculation(num1,num2)

if __name__ == "__main__":
    main()
