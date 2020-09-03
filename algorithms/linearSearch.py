# DSA: Data Structures Algorithms - Linear Search
'''
---------------------------------ALGORITHM---------------------------------
Linear Search (Array A, Value x)
Step 1: Set i to 1
Step 2: If i > n then go to step 7
Step 3: if A[i] = x then go to step 6
Step 4: Set i to i + 1
Step 5: Go to step 2
Step 6: Print Element x Found at index i
        and go to step 8
Step 7: Print element not found
Step 8: Exit
'''
# Function Search here
def search(arr, x, n):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = search(arr, x, n)
print("Element is not present in the array.") if result == -1 else print("Element is present at index ", result)

