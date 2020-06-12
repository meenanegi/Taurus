import random
print("    **** Guessing Game ****  ")
SecretNumber = random.randint(1,1000)
print(f"Secret Number is {SecretNumber}")
Chances = 0
while Chances<=2:
    Number = int(input("Guess the Numbe between 1 and 1000 : "))
    if Number!=SecretNumber:
        print("You guessed the wrong number, Try once again")
    else:
        print("You won the game")
        break
        Chances +=1
        print("You lose the game")


