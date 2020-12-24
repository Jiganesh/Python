# https://codeforces.com/problemset/problem/59/A
# Code Forces Easy Problems

upper = lower =0
string = input()
for i in string:
    if i.isupper():
        upper+=1
    else:
        lower+=1

print(string.upper() if upper>lower else string.lower())