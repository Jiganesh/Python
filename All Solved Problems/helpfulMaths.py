# https://codeforces.com/problemset/problem/339/A
# Code Forces Easy Problem

given = list(map(str, input().split("+")))
given.sort()
print("+".join(given))

# One Liner
print("+".join(sorted(input().split("+"))))
