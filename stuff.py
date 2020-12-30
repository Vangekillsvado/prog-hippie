
def compare(guess, number):
  if guess > number:
    return 1
  elif guess < number:
    return -1
  else:
    return 0

def factors(number):
  i = 2
  while i < 25:
    if number % i == 0:
      fac = str(i)
      return fac
  i = i+1
  return "prime"

def binaryHint(theNum, guess):
  ans = compare(guess, theNum)
  while True:
      if ans == 1:
          print("The number is less then " + str(guess))

      elif ans == -1:
          print("The number is greater then " + str(guess))
      if ans == 0:
          break
      guess = input("Enter a number")
      g = int(guess)
      ans = compare(g, theNum)



def hints(number, index):
  h = []
  
  if factors(number) == "prime":
    h.append("The number is a prime number.")
  else:
    h.append("The number is divisible by " + factors(number))
  return h[index]  



  