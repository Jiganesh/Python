# https://codeforces.com/problemset/problem/282/A
# Code Forces Easy Problem

n=int(input())
current = 0

while n:
    operation = input().replace(" ","")
    add = ["X++","++X"]
    subtract = ["X--","--X"]
    if operation in add:
        current+=1
    if operation in subtract:
        current-=1
    n-=1
print(current)