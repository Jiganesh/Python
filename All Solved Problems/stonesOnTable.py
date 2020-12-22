# https://codeforces.com/problemset/problem/266/A
# Code Forces Easy Problem

no_of_stones = int(input())
stones = input()

count = whole = 0
for i in range(1, no_of_stones):
    if stones[i-1] == stones[i]:
        count += 1

print(count)
