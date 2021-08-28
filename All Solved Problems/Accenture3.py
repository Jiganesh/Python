def balancedsum(array):

    array.sort()
    i=0
    j=len(array)
    while i<j:
        if sum(array[0:i])<=sum(array[j:]):
            i+=1
        else:
            j-=1
    return sum(array[:i])


array =[1,2,3,4,5,6]
print(balancedsum(array))