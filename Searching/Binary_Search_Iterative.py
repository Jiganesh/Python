# Searching Algorithms

def binarysearch_iterative(array, l, r, find):
    while l <= r:
        mid = l + (r-l)//2

        if array[mid] == find:
            return mid
        elif array[mid] < find:
            l = mid+1
        else:
            r = mid-1
    return -1


print(binarysearch_iterative([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10, 5))
