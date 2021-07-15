"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def dividing(arr, low, high):
    i = (low-1)         
    last = arr[high]     
  
    for j in range(low, high):
        if arr[j] <= last:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = dividing(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
def quicksort(array):
	# Your code goes here
	low=0
	high=len(array)-1
	quickSort(array, low, high)
	return array
