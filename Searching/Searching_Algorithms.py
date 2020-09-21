#Searching Algorithms

def linearsearch(array, find):
          n=len(array)
          for i in range (n):
                    if array[i] == find:
                              return i
          return -1

def binarysearch_iterative(array,l,r,find):
          while l<=r:
                    mid=l+(r-l)//2

                    if array[mid]== find:
                              return mid
                    elif array[mid]< find:
                              l=mid+1
                    else: 
                              r=mid-1
          return -1


def binarysearch_recursive(array,l,r,find):
          if l<=r:
                    mid= l +(r-l)//2
                    if array[mid]==find:
                              return mid
                    elif array[mid]< find:
                              return binarysearch_recursive(array,mid+1,r,find)
                    else:
                              return binarysearch_recursive(array,l,mid-1,find)

          return -1

array=[1,2,3,4,5,6,7,8]
print(binarysearch_recursive(array,0,len(array)-1,6))
