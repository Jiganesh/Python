# https://codeforces.com/problemset/problem/231/A
# Code Forces Easy Problem

problemNo = int(input())
cansolve = 0

while problemNo:
    sure = 0
    array = list(map(int, input().split()))

    for i in array:
        if i == 1:
            sure += 1

    if sure >= 2:
        cansolve += 1

    problemNo -= 1

print(cansolve)
