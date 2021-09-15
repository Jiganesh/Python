r = lambda a, c =0: c if len(a)==0 else  r(a[:a.index(max(a))],c+1)
n ,a= int(input()), list(map(int, input().split(",")))
print(r(a))
