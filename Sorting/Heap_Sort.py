#Sorting Algorithms

def heapify(array,n,i):
          largest=i
          l=i*2+1
          r=i*2+2

          if l< n and array[l]>array[largest]:
                    largest=l
          if r<n and array[r]>array[largest]:
                    largest=r
          if largest !=i:
                    array[largest],array[i]=array[i],array[largest]
                    heapify(array,n,largest)
                    
def heapsort(array,n):
          for i in range(n//2,-1,-1):
                    heapify(array,n,i)
          for i in range(n-1,-1,-1):
                    array[i],array[0]=array[0],array[i]
                    heapify(array,i,0)
          return array

print(heapsort([9,9,2,3,4,2,4,1,7,9],10))                    
