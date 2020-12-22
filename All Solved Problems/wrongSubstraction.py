# https://codeforces.com/problemset/problem/977/A
# Code Forces Easy Problem

m,n = map (int, input().split())

while n:
    if m%10 :
        m-=1
    else:
        m=m//10
    n-=1
print(m)