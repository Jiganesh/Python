import math

def numOfWays(nums):
        mod = 10 ** 9 + 7
        
        def dfs(num):
            if len(num) <= 1: return 1
            left = [n for n in num[1:] if n < num[0]]
            right = [n for n in num[1:] if n > num[0]]
            return len(num) * dfs(left) * dfs(right)
            
        return (math.factorial(len(nums)) // dfs(nums) - 1) % mod

array = list(map(int, input().split()))
print(numOfWays(array))