import random
import string

# Function to generate a random password
def password_generated(length=12):
    # Define all possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by picking characters randomly from the list
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Return the generated password
    return password

# Ask the user to enter the desired length of the password
length = int(input("Enter the length of your desired password: "))

# Generate the password using the function
password = password_generated(length)

# Print the generated password
print("Your desired generated password:", password)

