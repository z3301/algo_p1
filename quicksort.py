import numpy as np
from numpy.random import seed
from numpy.random import shuffle

# function to  find partition position
def partition(arr, low, high):
    # set pivot to high
    pivot = arr[high]
    # pointer for greater element
    i = low - 1
    # iterate through array
    for j in range(low, high):
        # if element is less than pivot
        if arr[j] <= pivot:
            # swap it with the element at i
            i = i + 1
            # swap elements i and j
            (arr[i], arr[j]) = (arr[j], arr[i])
    # swap pivot with element at i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    # return index of pivot
    return i + 1

# function to sort array
def quicksort(arr, low, high):
    # if start index is less than end index
    if low < high:
        # set partition index
        piv = partition(arr, low, high)
        # recursive call to sort smaller elements
        quicksort(arr, low, piv - 1)
        # recursive call to sort larger elements
        quicksort(arr, piv + 1, high)

# hard-coded array
arr = [ 10, 80, 3, 19, 14, 7, 5, 12 ]
# call quicksort for hard-coded arr
quicksort(arr, 0, len(arr) - 1)
print(f'Sorted hard-coded array: {arr}')

# seed a numpy random number generator
seed(1)
# prepare a sequence of 100
seq = [i for i in range(100)]
# shuffle the sequence
shuffle(seq)
# convert sequence list to numpy array
seq_arr = np.array(seq)
# call quicksort function
quicksort(seq_arr, 0, len(seq_arr) - 1)
print(f'Sorted array of 100: {seq_arr}')

# seed a new numpy random number generator
seed(2)
# prepare a sequence of 1000
seq = [i for i in range(1000)]
# randomly shuffle the sequence
shuffle(seq)
# convert sequence list to numpy array
seq_arr = np.array(seq)
# call quicksort function
quicksort(seq_arr, 0, len(seq_arr) - 1)
print(f'Sorted array of 1000: {seq_arr}')