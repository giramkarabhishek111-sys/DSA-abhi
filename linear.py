# Linear search implementation
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return -1  


# Binary search implementation
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:  
        mid = (low + high) //2
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            low = mid + 1  
        else:
            high = mid - 1 
            
    return -1  


# Main program execution
n = int(input("Enter number of customer account ID's: "))
print("Enter the account ID's in sorted order (separated by space):")


arr = list(map(int, input().split()))

key = int(input("Enter customer account ID to search: "))


# --- Executing Linear Search ---
linear_result = linear_search(arr, key)
if linear_result != -1:
    print(f"Linear Search: Account ID found at index {linear_result}")
else:
    print("Linear Search: Account ID not found.")


# --- Executing Binary Search ---
binary_result = binary_search(arr, key)
if binary_result != -1:
    print(f"Binary Search: Account ID found at index {binary_result}")
else:
    print("Binary Search: Account ID not found.")
