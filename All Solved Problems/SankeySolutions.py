def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

n = int(input())
array = list(map(int, input().split()))
sum =start = end =0
allabs = []
number = array[0]
for number in set(array):
    p = abs(listRightIndex(array,number) - array.index(number))
    allabs.append(p)
    sum += p
    if max(allabs) == p:
        start = array.index(number)+1
        end = listRightIndex(array,number)+1  
        num = number

        
print("Sum = ",sum)
print("Position = ",(start,end))
print("Number = " ,num)