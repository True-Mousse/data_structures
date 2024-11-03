## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT
## Mid Term: Question 1

input = "({[]})" # Balanced

# input = "({[})]" # Not Balanced


list_A = [] # Create empty List 

# Creates List w/ First 1/2 of String 
for i in range(int(len(input)/2)):
  list_A += input[i]
print("First 1/2 of String: ", list_A)

list_B = [] # Create empty List

# Creates List w/ BVottom 1/2 of String
for i in range(int(len(input)/2), len(input)):
  list_B += input[i]
print("Bottom 1/2 of String: ", list_B)

true_counter = 0 # Total Number of Times Balanced

# Comparison Loop of List A vs List B
# Every time there is a match that is TRUE, add +1 to 
# true_counter. 
for i in range(int(len(input)/2)):
  if list_A[i] == "(" and list_B[i] == ")":
    true_counter += 1
  elif list_A[i] == "[" and list_B[i] == "]":
    true_counter += 1
  elif list_A[i] == "{" and list_B[i] == "}":
    true_counter += 1

# If top & bottom 1/2 of input is TRUE, then the 
# true_counter value is == to 1/2 of the length of the input
print("\nFinal Answer: ")
if true_counter == int(len(input)/2):
  print("Balanced")
else:
  print("Not Balanced") 
    
