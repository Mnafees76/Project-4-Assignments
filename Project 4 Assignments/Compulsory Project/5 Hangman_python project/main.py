import random

# List of words to choose from
words_list = ["python", "hangman", "challenge"]

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed and unguessed letters hidden
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter  # Show guessed letter
        else:
            display += "_"  # Hide unguessed letter
    return display

def Hangman():
    # Main function to run the Hangman game
    word = random.choice(words_list)  # Select a random word
    guessed_letters = set()  # Store guessed letters
    attempts = 6  # Set number of attempts

    print("Welcome to Hangman!")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Attempts Left: {attempts}")

        guess = input("Enter a letter: ").lower()  # Get user input

        if guess in guessed_letters:
            print("You already guessed this letter. Try again.")
            continue  # Skip if letter was already guessed

        guessed_letters.add(guess)  # Add guessed letter to the set

        if guess in word:
            print("You guessed a correct letter!")
        else:
            print("Your guessed letter is wrong.")
            attempts -= 1  # Reduce attempts if guess is incorrect

        if "_" not in display_word(word, guessed_letters):  # Check if word is fully guessed
            print(f"Congratulations! You guessed the word '{word}'.")
            break

    if attempts == 0:
        print(f"Game over! The correct word was '{word}'.")

# Start the game
Hangman()
