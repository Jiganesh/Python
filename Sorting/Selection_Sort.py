#Sorting Algorithms

def selectionsort(array):
          n=len(array)
          for i in range (n):
                    mini=i
                    for j in range(i+1,n):
                              if array[mini]>= array[j]:
                                        mini=j
                    array[mini],array[i]=array[i],array[mini]
          return array

print(selectionsort([8,6,4,6,8,2,5,0,9,1,6,7]))
