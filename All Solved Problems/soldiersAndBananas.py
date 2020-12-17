# https://codeforces.com/problemset/problem/546/A
# Code Forces Easy Problem

a, b, c = map(int, input().split())

multiplier = 1
total = 0
while c:
    total += multiplier * a
    multiplier += 1
    c -= 1

print(total - b if total - b >= 0 else 0)
