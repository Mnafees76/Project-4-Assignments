# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:


# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.  #Anton is 21


# Ethan is the same age as Chen.

def main():
    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20
    Drew = Anton + Beth
    Ethan = Chen
    
    print(f"Anton age is = {Anton}")
    print(f"Beth age is =  {Beth}")
    print(f"Chen age is = {Chen}")
    print(f"Drew age is = {Drew}")
    print(f"Ethan age is = {Ethan}")

main()

