# https://codeforces.com/problemset/problem/116/A
# Code Forces Easy Problem

n=int(input())
maximum=count=0
while n:
    out,enter = map(int,input().split())
    count += enter
    count-= out
    maximum =max(count, maximum)
    n-=1
print(maximum)