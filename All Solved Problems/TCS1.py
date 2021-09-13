n = int(input())
array = [i for i in input() if i.isalnum()]
p= [i for i in array if array.count(i)&1][0]
print(p[0] if p else "All are even")