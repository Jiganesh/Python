# https://codeforces.com/problemset/problem/112/A
# Code Forces Easy Problem

string1=input().lower()
string2=input().lower()

print(-1 if string2>string1 else 0 if string1==string2 else 1)