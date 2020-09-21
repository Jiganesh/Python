#Sorting Algorithms

def insertionsort(array):
          n=len(array)
          for i in range (n):
                    key=array[i]
                    j=i-1
                    while j>=0 and key<array[j]:
                              array[j+1]=array[j]
                              j-=1

                    array[j+1]=key
          return array

print(insertionsort([8,3,6,2,5,3,7,0,7,2,4,2]))
