# https://codeforces.com/problemset/problem/263/A
# Code Forces Easy Problem

for i in range (5):
    array = list(map(int,input().split()))
    for j in range (5):
        if array[j]==1:
            row,column = i,j
    
print(abs(2-row)+abs(2-column))