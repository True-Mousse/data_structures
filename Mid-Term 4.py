## Author:  Michael K. Javner
## Class:   TINFO 501
## Program: MSIT
## Mid Term: Question 4

# Write a function to perform a binary search on a sorted array to find the index of a given value. If the target is not found, return -1

# Input: arr = [1,2,3,4,5], target = 3
# Output: 2

# Input: arr = [1,2,3,4,5], target = 6
# Output: -1

# Input: arr = [2,4,6,8,10], target = 6
# Output: 2

def binary_search(arr, target):

    # Returnes -1 if target is less than value held in first element or greater than last element
    # Only works if array is in-order
    if (arr[0] > target or arr[len(arr)-1] < target):
        return -1
        
    # If target value is found, returns position in array    
    if arr[len(arr)//2] == target:
        return len(arr)//2
    
    # Bottom elif statements split the array in 1/2 based on mid-point

    # If target value is greater than mid-point, creates 2nd array from
    # mid-point to end. Recursion used to deep dive. Position in array 
    # added together to locate the TRUE position in original array
    elif (target > arr[len(arr)//2]):
        #print(arr)
        return len(arr)//2 + binary_search(arr[len(arr)//2:], target)
        
    # If the target value is less than mid-point, creates 2nd array from 
    # beginning to mid-point. Recursion again used to deep dive. Addition not 
    # used since using the original position of array.     
    elif (target < arr[len(arr)//2]):
        return binary_search(arr[:len(arr)//2], target)

    

def main():

    arr = [2,4,6,8,10]
    target = 6

    print(binary_search(arr, target))


main()
    
