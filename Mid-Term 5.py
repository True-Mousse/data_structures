## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT
## Mid Term: Question 5

def sum_of_elements(list):
    
    sum = 0 # Total Value

    if list == []: # Stops Recursion 
        return 0
    
    sum = list.pop() + sum_of_elements(list) # Pop removes final Element in List & re-summon itself
                         
    return sum
    

def main():

    test_A = [1, 2, 3, 4, 5]
    print("[1, 2, 3, 4, 5]")
    print("Test A: ", sum_of_elements(test_A))
    print("") 
    
    test_B = [10, -2, 3, 7]
    print([10, -2, 3, 7])
    print("Test B: ", sum_of_elements(test_B))
    print("") 

    test_C = []
    print("[]")
    print("Test C: ", sum_of_elements(test_C))
    print("") 

main()