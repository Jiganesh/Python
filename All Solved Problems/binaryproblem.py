n =input()
l = int(input())
result=[]
while len(n)>l:
    result.append(n[:l])
    n=n[l:]

result.append(n)

answer = sorted([i.count('1'),i] for i in result)[-1][-1]
print(int(answer,2))