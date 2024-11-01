## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT

########################
# Stack Data Strucutre #
########################
class Stack:

    # Initial constructor that builds the Array when the Object is created 
    def __init__(self, capacity):
        self.stack = [None] * capacity # Builds the Stack Array; None is used as placeholder
        self.top = -1 # Top of Stack in Stack Array
        self.size = 0  # Number of Elements in Stack 

    # Returns the number of elements in Stack
    def size(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.size]
    
    # Checks if Stack Array holds any Elements 
    #   Returns: True/False
    def is_empty(self):
        return self.size == 0

    # Adds Element to Stack Array
    def push(self, item):
        # Validates if Stack Array is Full
        if (self.size == len(self.stack)): 
            print("Stack is full")
            return
        else:
          self.top += 1 # Location of Last Out position in Stack
          self.stack[self.top] = item # Adds Element to Top of Stack Array
          self.size += 1 # Increase Size by 1 reflecting the additional Element added to the Stack Array

    # Removes Element from Top of Array 
    def pop(self):
        # Validates if Queue Array is Empty
        if self.is_empty():
            print("Queue is empty")
            return None

        item = self.stack[self.top] # Stores Element in Front of Queue Array into item variable
        self.stack[self.top] = None # Remove the Value from Queue Array
        self.top -= 1 # Drops the Top position by 1
        self.size -= 1 # Decreases Size by 1 reflecting the Element being removed from Queue Array
        return item 

    # Returns 1st Element in Queue Array w/o modifying Array
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.stack[self.top]

def main():
    
    # Asks user the length of Stack array
    s_length = int(input("Length of Stack? "))

    stack_A = Stack(s_length) # Main Stack array
    stack_B = Stack(s_length) # Placeholder Stack array 

    # Adds Elements to the Stack Array
    for i in range(0, s_length):
        userInput = input("Please input a single character: ")
        stack_A.push(userInput)


    print("Stack A: ", stack_A.stack)
    print("Peek Stack A: ", stack_A.peek())
    print("Pop Stack A: ", stack_A.pop())
    print("Stack A: ", stack_A.stack)
###########
# Dequeue # 
###########
    # Prints & Removes the First Element of the Stack 
    # Moves elements to stack_B until First-In Element of stack_A reached
    for i in range(1, stack_A.size):
        stack_B.push(stack_A.pop())

    print("Dequeue: ", stack_A.pop())
    for i in range(0, stack_B.size):
        stack_A.push(stack_B.pop())

    print("Final Stack A:", stack_A.stack)
    print("Final Stack B:", stack_B.stack)

###########
# Enqueue #  
 ##########   
    # Adds an Element to the Stack
    userInput = input("Please input a single character: ")
    print("Enqueue: " + userInput)
    stack_A.push(userInput)

    print("Final Stack A:", stack_A.stack)
    print("Final Stack B:", stack_B.stack)
main()
