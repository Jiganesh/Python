
def minimumCost(arr,N):
    result=[]
    for i in arr: 
        sumofall =0
        for j in arr:
            sumofall += abs(j-i)
        result.append(sumofall)
    return min(result)




print(minimumCost([2,3,1,4,5],5))
print(minimumCost([1,4,7,8,10,3,2,5,6,9],10))