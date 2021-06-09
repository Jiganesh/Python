def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0

    smallest = float("inf")
    current = float("inf")

    smallestPair=[]
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):

        current = abs(arrayOne[idxOne]-arrayTwo[idxTwo])
        if current < smallest:
            smallest =current
            smallestPair = [arrayOne[idxOne],arrayTwo[idxTwo]]

        if arrayOne[idxOne]<arrayTwo[idxTwo]:
            idxOne +=1
        else: 
            idxTwo+=1
    return smallestPair

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))
print(smallestDifference([1, 3, 15, 11, 2],[23, 127, 235, 19, 8]))
print(smallestDifference([10, 5, 40],[50, 90, 80]))
print(smallestDifference([1, 2, 11, 15],[4, 12, 19, 23, 127, 235]))
print(smallestDifference([1, 2],[3,4]))
print(smallestDifference([1],[4]))

