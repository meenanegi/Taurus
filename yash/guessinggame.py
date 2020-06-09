import random
i = 0
number = random.radiant(1, 11)

while i != 3:
    secret_number = int(input("enter any number : "))

    if secret_number != number:
        print("you guess wrong number.")
    else:
        print("you guesses it you win.")
        break
    i += 1
print("You lose")


