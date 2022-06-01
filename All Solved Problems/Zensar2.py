n = int(input())

def isPrimeOrNot(n):
    if n <= 2: return False
    return all(n%i for i in range(2,int(n**0.5)+1))
array=[]
p=5
a=n
while p and a >=0:
    if (isPrimeOrNot(a)):
        array.append(a)
        p-=1
    a-=1
    
p=5
a=n
while p:
    if (isPrimeOrNot(a)):
        array.append(a)
        p-=1
    a+=1
ans = sorted(array, key= lambda x: abs(n-x))[:5]
res = min([i for i in ans if abs(n-ans[-1])==abs(n-i)])
print(res)
    

