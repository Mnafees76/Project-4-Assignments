# Guess the Number - Python Project (Computer)
import random

def guess_the_number():
    """Project: Guess The Number Game By Computer."""
    
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    
    # Set the number of guesses allowed
    guesses_left = 5
    
    print("I am thinking of a number between 1 to 10.")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        
        # Get user input and handle invalid input
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input: Please enter a valid number.")
            continue
        
        # Check if the guessed number is too low
        if guess < number:
            print("Too low! Try again.")
        
        # Check if the guessed number is too high
        elif guess > number:
            print("Too high! Try again.")
        
        # If the guessed number is correct
        else:
            print(f"Congratulations! You guessed the correct number in {5 - guesses_left + 1} tries.")
            return  # Exit the function if the guess is correct
        
        # Reduce the number of guesses left
        guesses_left -= 1

    # If user runs out of guesses, reveal the correct number
    print(f"\nYou ran out of guesses. The correct number was {number}.")

# Call the function to start the game
guess_the_number()
