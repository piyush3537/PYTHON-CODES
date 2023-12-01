

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
guess = None

print("Welcome to the Number Guessing Game!")

# Main game loop
while guess != secret_number:
    try:
        # Get user's guess as an integer
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")

# End of the game
