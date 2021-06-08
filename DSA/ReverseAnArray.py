array = [1,2,3,4,5]

i= 0
j= len(array)-1

while i < j:
    array[i],array[j]=array[j],array[i]
    i+=1
    j-=1

print(array)

'''

Basically you put two pointers one at start of array and another one at end of array.
you traverse the array swapping those two places with each other and moving forward from both directions

'''