




 # Get a positive integer input from the user
try:
    num = int(input("Enter a positive integer: "))
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Check if the input is a positive integer
if num < 0:
    print("Please enter a positive integer.")
else:
    # Initialize variables
    factorial = 1
    current_num = 1

    # Calculate the factorial using a while loop
    while current_num <= num:
        factorial *= current_num
        current_num += 1

    # Print the factorial
    print(f"The factorial of {num} is {factorial}")

