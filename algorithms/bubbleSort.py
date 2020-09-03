# DSA: Data Structures Algorithms - BubbleSort
'''
----------------------ALGORITHM----------------------
* Bubble Sort is the simplest sorting algorithm that works by 
repeatedly swapping the adjacent elements if they are in wrong order.

'''
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [27, 43, 42, 56, 65, 12, 89, 39, 39]
bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print(arr[i], end=' ')