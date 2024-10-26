## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT

########################
# Queue Data Strucutre #
########################
class Queue:

    # Initial constructor that builds the Array when the Object is created 
    def __init__(self, capacity):
        self.queue = [None] * capacity # Builds the Queue Array; None is used as placeholder
        self.front = 0 # Location of Front of Queue
        self.rear = -1 # Location of End of Queue
        self.size = 0  # Number of Elements in Queue 

    # Checks if Queue Array holds any Elements 
    #   Returns: True/False
    def is_empty(self):
        return self.size == 0

    # Adds Element to Queue Array
    def enqueue(self, item):
        # Validates if Queue Array is Full
        if (self.size == len(self.queue)): 
            print("Queue is full")
            return
        else:
          self.rear = (self.rear + 1) % len(self.queue) # Changes End of Queue position by 1 to reflect circular Queue positioning
          self.queue[self.rear] = item # Adds Element to End of Queue Array
          self.size += 1 # Increase Size by 1 reflecting the additional Element added to the Qeueu Array

    # Removes Element from Queue Array 
    def dequeue(self):
        # Validates if Queue Array is Empty
        if self.is_empty():
            print("Queue is empty")
            return None

        item = self.queue[self.front] # Stores Element in Front of Queue Array into item variable
        self.queue[self.front] = None # Remove the Value from Queue Array
        self.front = (self.front + 1) % len(self.queue) # Changes position in Queue Array by 1 to reflect circular Queue positioning
        self.size -= 1 # Decreases Size by 1 reflecting the Element being removed from Queue Array
        return item 

    # Returns 1st Element in Queue Array w/o modifying Array
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.queue[self.front]

def main():
    
    # Asks user the length of Queue
    q_length = int(input("Length of Queue? "))

    queue_A = Queue(q_length) # Main Queue
    queue_B = Queue(q_length) # Secondary Queue (Placeholder)

    # Adds Elements to the Main Queue Array
    for i in range(0, q_length):
        userInput = input("Please input a single character: ")
        queue_A.enqueue(userInput)

    
#######
# PoP # 
#######

    print("Start: Queue_A = ", queue_A.queue)
    #print("Location of Rear: ", queue_A.rear)
    print("Location of Rear: ", queue_A.queue[queue_A.rear])
    queue_A.queue[queue_A.rear] = [None]
    queue_A.rear -= 1
    queue_A.size -= 1
    print("End of Queue_A = ", queue_A.queue)
    print("Rear # :", queue_A.rear)


########
# Push #
########

    userInput = input("Please input a single character: ")
    print("Push: " + userInput)
    queue_A.enqueue(userInput)

    print("Final Stack A:", queue_A.queue)

main()
