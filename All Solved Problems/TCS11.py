n = int(input())
array =[]
for i in range (n):
    array.append(int(input()))

count =0

for i in range (0, n):
    for j in range(1,n):
        if i*j == array[i]*array[j]:
            count+=1
print(count)