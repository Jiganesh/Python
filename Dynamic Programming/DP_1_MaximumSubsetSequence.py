#Maximum Subset Sum No Adjacent

def maxsubsetsum(array):

          maxsub=array[:]
          maxsub[1]=max(array[0],array[1])

          for i in range (2, len(array)):
                    maxsub[i]= max(maxsub[i-1],maxsub[i-2]+maxsub[i])
          return maxsub[-1]


array = [7,10,12,7,9,14]
print(maxsubsetsum(array))
