n = int(input())
a = [i**2 for i in range(n)]
count=0
for i in a :
    if n<=i:
        print(count)
        break
    n-=i
    count+=1
    