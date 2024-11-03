## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT
## Mid Term: Question 3

# Formual
# SPARK(n) = 2^1 + 2^2 + 2^3 + 2^n

def SPARK(n):

  if (n == 0): # Stops the Recursion
    return 0
  
  elif (n < 0):
    return("The Number Entered is Less than 0.")
  
  elif (n > 30):
    return("The Number Entered is Greater than 30.")
  
  else:
    return 2 ** n +  SPARK(n-1) # 2 ^ (n-1)

def main():

  n  = int(input("Enter a Number Between 0 - 30: "))

  print(SPARK(n))

main()
