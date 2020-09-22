#Sorting Algorithms

def bubblesort(array):
          n=len(array)
          for i in range(n):
                    for j in range(n-i-1):
                              if array[j]>=array[j+1]:
                                        array[j],array[j+1]=array[j+1],array[j]
          return array

print(bubblesort([8,6,4,6,8,2,5,0,9,1,6,7,20,30]))
