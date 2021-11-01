n = int(input())
a=sum([i for i in range(1,n) if n%i==0])
print(1 if a == n else a)
