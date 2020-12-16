# https://codeforces.com/problemset/problem/281/A
# Code Forces Easy Problem

string = list(input())
string[0]=chr(ord(string[0])-32) if ord(string[0])>96 else string[0]
print("".join(string))
