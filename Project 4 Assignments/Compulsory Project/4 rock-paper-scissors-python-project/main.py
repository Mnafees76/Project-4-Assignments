import random

# List of choices for the game
choices = ["rock", "paper", "scissors"]

while True:
    # Asking user to input their choice
    user_choice = input("🎮 Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").strip().lower()

    # Check if user wants to exit the game
    if user_choice == "exit":
        print("👋 Thanks for playing! Goodbye!")
        break

    # Validate user input
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter only 'Rock', 'Paper', or 'Scissors'.")
        continue

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice.capitalize()}")

    # Checking the result of the game
    if user_choice == computer_choice:
        print("😐 It's a Draw! Both chose the same.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You Win! Congratulations! 🏆")
    else:
        print("💻 Computer Wins! Better luck next time! 😔")

    # Asking the user if they want to play again
    play_again = input("🔄 Do you want to play again? (Yes/No): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing! See you next time!")
        break