# https://codeforces.com/problemset/problem/158/A
# Code Forces Easy Problem

n, k = map(int, input().split())
array = list(map(int, input().split()))

kthplace = array[k-1]
count = 0
for i in range(n):
    if array[i] > 0 and array[i] >= kthplace:
        count += 1
print(count)
