import math
def factors(n):
    return sum([i for i in range(1, n) if n % i == 0])

n = int(input())
a = factors(n)
print(1 if factors(a) == n else 0)



