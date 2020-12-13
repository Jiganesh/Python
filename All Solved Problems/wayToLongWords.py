# https://codeforces.com/problemset/problem/71/A
# Code Forces Easy Problem

testcase = int(input())
while testcase:
    count=0
    word = input()
    for i in word:
        if i != " ":
            count += 1
    if count > 10:
        print("{}{}{}".format(word[0], count-2, i))
    else:
        print(word)

    testcase -= 1
