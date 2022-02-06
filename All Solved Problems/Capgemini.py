n = int(input())
array= []
while n:
    array.append(int(input()))
    n-=1
    
def maxP(prices, days):
    return sum(prices[i] - prices[i-1] for i in range(1, days) if prices[i] > prices[i-1])

print(maxP(array,len(array)))
