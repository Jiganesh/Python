array =[10,9,2,4,5,9,1,12,8,7]

n = len(array)
if n&1:
    mi=mx=array[0]
    i=1
else:
    mi = min(array[0],array[1])
    mx = max(array[0],array[1])
    i=2

while i<n:

    if array[i]> array[i+1]:
        if array[i]>mx:
            mx=array[i]
        if array[i+1]<mi:
            mi=array[i+1]

    else:
        if array[i]<mi:
            mi=array[i]
        if array[i+1]>mx:
            mx=array[i+1]
    i+=2

print(mi,mx)

'''

Time Complexity = 3 *(n-1)//2
As we are taking in pairs it is half we are not checking the first element so n-1
and 3 constant time operations of if hence it will be that and space complexity in n

'''