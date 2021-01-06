m,n = map(int, input().split())
string = list(input())

while n:
    for j in range (0,m-1):
        if string[j] =="B" and string[j+1]=="G":
            string [j] ,string[j+1]=string[j+1],string[j]
    n-=1
print(string)


