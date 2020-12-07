# https://bit.ly/3mPTgEb

n,m =map(int, input().split ())
array =list(map(int, input().split ()))
m=m%n
a=array[m:]+array[:m]
print(*a)