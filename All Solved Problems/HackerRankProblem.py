n = int(input())
stack=[]
while n:
    string = input()
    if "1" == string[0]:
        op , num = map(int,string.split())
        stack.append(max(stack[-1]),num)
    elif "2" ==string[0]:
        stack.pop()
    else:
        print(stack[-1])
    n-=1

# HackerRank Problem Name = Maximum Elements

