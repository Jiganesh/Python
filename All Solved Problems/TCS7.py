n= int(input())
if 10<=n and n<=1000000:
    a=[int(i)**2 for i in str(n)]
    print("".join(map(str,a))[::-1])
else:
    print("Wrong Input")