n = int(input())

array =[]
while n:
    array.append(input().split(","))
    n-=1
    
result = []

for s, r in array:
    r = int(r)% len(s)
    rstring = s[-r:]+s[:-r]
    print(rstring, r)
    ans = "".join([rstring[i] for i in range(len(rstring)) if (i+1)%2==0 and rstring[i].lower() in "qwrtypsdfghjklzxcvbnm"])
    if len(ans)>=1:
        result.append(ans)
    
result = sorted(result, key = len)

if result :print(*result, sep=",")
else : print(-1)
    
"""
4
knowledge,3
education,1
elepHant,5
building,2

2
aaieo,2
education,1

5
   ,0
 ,4
  D,9
  ,1
  ,1
  
"""