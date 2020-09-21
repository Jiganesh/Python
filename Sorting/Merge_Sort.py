#Sorting Algorithms

def mergesort(array):
          if len(array)>1:
                    mid=len(array)//2
                    L=array[:mid]
                    R=array[mid:]
                    mergesort(L)
                    mergesort(R)
                    i=j=k=0

                    while i <len(L) and j< len(R):
                              if L[i]<R[j]:
                                        array[k]=L[i]
                                        i+=1
                              else:
                                        array[k]=R[j]
                                        j+=1
                              k+=1

                    while i <len(L) :
                              array[k]=L[i]
                              i+=1
                              k+=1
                    while j <len(R):
                              array[k]=R[j]
                              j+=1
                              k+=1
          return array


print(mergesort([9,7,4,9,2,4,6,7,5,1,0,2,8,2,0]))
