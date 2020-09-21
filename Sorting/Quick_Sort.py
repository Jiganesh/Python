#Sorting Algorithms

def partition(array,low,high):
          i=low-1
          pivot=array[high]

          for j in range(low,high):
                    if array[j]<pivot:
                              i+=1
                              array[j],array[i]=array[i],array[j]
          array[i+1],array[high]=array[high],array[i+1]

          return(i+1)

def quicksort(array,low,high):
          if low<high:
                    pi=partition(array,low,high)
                    quicksort(array,low,pi-1)
                    quicksort(array,pi+1,high)
          return array

array=[7,9,3,5,6,7,9,1,2,9,3,7,3,9,0,4]
low=0
high=len(array)-1
print(quicksort(array,low,high ))
