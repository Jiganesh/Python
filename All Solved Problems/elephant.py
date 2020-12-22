# https://codeforces.com/problemset/problem/617/A
# Code Forces Easy Problem

n=int(input())
count=0
m=5
while n:
    if n>=m:
        count+=1
        n-=m
    else:
        m-=1
print(count) 