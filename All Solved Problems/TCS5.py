s= lambda x: sum([i for i in str(x)])
n,p = s(input()), int(input())
print(s(n*p))