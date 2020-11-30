# Sorting Algorithms

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def selectionsort(array):
    n = len(array)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if array[mini] >= array[j]:
                mini = j
        array[mini], array[i] = array[i], array[mini]
    return array


def insertionsort(array):
    n = len(array)
    for i in range(n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array


def partition(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return(i+1)


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
    return array


def heapify(array, n, i):
    largest = i
    l = i*2+1
    r = i*2+2

    if l < n and array[l] > array[largest]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)


def heapsort(array, n):
    for i in range(n//2-1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array
