arr = list(map(int, input().split(",")))
innum=  int(input())
output =[]

def permutations(arr, innum,  result=[]):
    if innum == 1:
        a = sorted(result[:])
        if a not in output:
            output.append(a)
        return
    else:
        for i in arr:
            
            if innum%i ==0:
                result.append(i)
                permutations(arr, innum//i, result)
                result.pop()

permutations(arr, innum, result=[])
        
output.sort()
if output:
    for i in output :
        print(*i , sep=",")
else:
    print(-1)

"""
2,4,6,8
16
"""