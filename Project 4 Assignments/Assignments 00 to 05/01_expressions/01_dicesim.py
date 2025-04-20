import random  # Ye library random numbers banane ke liye use hoti hai.

NUM_SIDES = 6  # Har die ke 6 sides hain. (Global variable)

def roll_dice():
    """
    Ye function 2 dice ko roll karta hai aur unka total print karta hai.
    """
    die1 = random.randint(1, NUM_SIDES)  # Pehla dice roll hota hai (1 se 6 tak)
    die2 = random.randint(1, NUM_SIDES)  # Dusra dice roll hota hai (1 se 6 tak)
    total = die1 + die2  # Dono ka total nikalta hai
    print("Total of two dice:", total)  # Total print hota hai

def main():
    die1 = 10  # Ye variable sirf `main()` ke andar kaam karega
    print("die1 in main() starts as: " + str(die1))  # Pehle iska value print hoga
    roll_dice()  # Pehli bar dice roll hoga
    roll_dice()  # Dusri bar dice roll hoga
    roll_dice()  # Teesri bar dice roll hoga
    print("die1 in main() is: " + str(die1))  # End me die1 ka value waisa hi rahega

if __name__ == '__main__':  # Program yahan se start hota hai
    main()
