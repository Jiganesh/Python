array =[12,4,3,9,6,8,10,14,11]
target =24


def ThreeSumTriplets(array,target):

    triplets =[]
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1

        while left < right: 

            currentsum = array[i]+array[left]+array[right]
            if currentsum == target:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif currentsum<target:
                left+=1
            elif currentsum>target:
                right-=1
    return triplets

print(ThreeSumTriplets(array,target))

