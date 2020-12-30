import random
import stuff
import hint 

n = random.randint(0,22)
guess = input("Guess a number between 0 and 22: ")
g = int(guess)

numTrys = 0
while stuff.compare(g, n) != 0:
    print(stuff.hints(g, numTrys))
    guess = input("Try again: ")
    g = int(guess)
    numTrys += 1

print ("Congrats")
