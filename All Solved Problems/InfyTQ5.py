n = int(input())
block = list(map(str, input().split(",")))
string = input()

def isValid(r, c , m):
    if r>=0 and r<m and c>=0 and c<m :
        return True
    
def direction (s):
    if s =="W":
        return [0,-1]
    if s =="E":
        return [0,1]
    if s == "N":
        return [-1,0]
    if s == "S":
        return [1,0]

result= [] 
current = [0,0]
for s in string :
    
    add = direction(s)
    newPath = [current[0]+add[0], current[1]+add[1]]
    
    if isValid(newPath[0], newPath[1], n)   and str(newPath[0]+1)+str(newPath[1]+1) not in block:
        current = newPath
        result.append([newPath[0]+1, newPath[1]+1])
    
    if current[0]==n-1 and current[1]==n-1:
        break
    
if result == []: print(-1)

if result and  (result[-1][0]!=n-1 or result[-1][1]!=n-1):
    print(-1)
else :
    a = ["".join(map(str,i)) for i in result]
    
    print(*a, sep=",")

"""
3
12,22,23
SESEWWEEN

2
21
EE
"""