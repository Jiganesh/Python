#Searching Algorithms

def linearsearch(array,find):
          n=len(array)
          for i in range(n):
                    if array[i]== find:
                              return i
          return -1

print(linearsearch([9,4,5,6,1,2,8,9],4))
