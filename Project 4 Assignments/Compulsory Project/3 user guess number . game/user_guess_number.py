import random

# Function to start the "Guess the Number" game
def Guess_number():
    print("Guess the number between 1 to 10")

    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    while True:
        try:
            # Get user's guess and ensure it's a valid integer
            guess = int(input("Enter your guessing number: "))

            # Check if the guess is too low
            if guess < number:
                print("Too Low! Try again.")

            # Check if the guess is too high
            elif guess > number:
                print("Too High! Try again.")

            # If guess is correct, print message and exit loop
            else:
                print("Congratulations! You guessed the right number!")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to start the game
Guess_number()


