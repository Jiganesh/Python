#Searching Algorithm

def binarysearch_recursive(array,l,r,find):
          if l<=r:
                    mid=l+(r-l)//2

                    if array[mid]==find:
                              return mid
                    
                    elif array[mid]<find:
                              return binarysearch_recursive(array,mid+1,r,find)

                    else:
                              return binarysearch_recursive(array,l,mid-1,find)
          return -1

print(binarysearch_recursive([0,1,2,3,4,5,6,7,8,9],0,10,5))
