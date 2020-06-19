#Program 3 - Guessing game
import random
setno=random.randint(1,10)

def guessnumber():
    g=input("Guess the secret number: ")
    g=int(g)
    return g

g=guessnumber()
i=1
while i<=3:
    
    if g==setno:
        print("You won")
        break
    elif i<3:
        i+=1
        g=guessnumber()
    else:
        print("You Lose")
        break 
