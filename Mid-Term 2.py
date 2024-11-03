## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT
## Mid Term: Question 2

# I could not solve this problem but I've written down my psuedo code. 
# I could not figure out the reversal function but it would have created
# smaller Qs going down. Then Enqueue itself back up to get the reversed process
# Once reversed, the main Queue would deQ itself into the 2nd Queue to finish the problem. 


def reversal(queue):
    
    tempQ = []
    if (len(queue) == 1):
        return queue

   
        
        

def main():

    queue_A = [1,2,3,4,5] # Main Q
    k = 3  # Reveral Location

    queue_B = [] # Secondary Q

    # For loop used to create the Array w/ the elements to be reversed
    for i in range(3):
        queue_B.append(queue_A.pop(0))
    
    reversal(queue_B)
    
    
main()