import random
n = random.randint(0,22)
guess = input("Enter a number")
pog = str(n)
print (guess + ", " + pog)
import stuff
import hint 
n = random.randint(0,22)

pog = str(n)

windex = 0
theNum = "The number is "
guess = input("Enter a number")
g = int(guess)
print (guess + ", " + pog)
ans = stuff.compare(g, n)
while True:
    if ans == 0:
        print("Congrats")
        break
    else:
        ##theHint = stuff.hint
        print(stuff.hints(g, windex))
        guess = input("Enter a number")
        g = int(guess)

