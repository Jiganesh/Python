
def Cards(cls,input1,input2):

    total_sum = sum(input2)

    max_sum = -99999999
    for i in range(input1):
        s = 0
        flip_sum = 0
 
        for j in range(i, input1):
            s += input2[j]
            max_sum = max(max_sum,total_sum - 2 * s)

    return max(max_sum, total_sum)
print(Cards(0,5,[-2,3,-1,-4,-2]))
print(Cards(0,5,[-1,2,3,4,-5]))
