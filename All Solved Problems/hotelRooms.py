# https://codeforces.com/problemset/problem/1200/A
# Code Forces Easy Problem

operations = int(input())
string = input()

def allot_left(room):
    i = 0
    while room[i] != "0":
        i += 1
    room[i] = "1"

def allot_right(room):
    i = -1
    while room[i] != "0":
        i -= 1
    room[i] = "1"

room = ["0" for i in range(0, 10)]

for i in string:
    if i == "L":
        allot_left(room)
    elif i == "R":
        allot_right(room)
    elif i.isnumeric():
        room[int(i)] = "0"

print("".join(map(str, room)))
