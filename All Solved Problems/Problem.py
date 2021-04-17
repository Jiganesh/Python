n = int(input())

if 0<n<=1000000: n=list(str(n)) ; result = "".join([str(9-int(i)) for i in n])
else: result="Wrong Input"

print(result)


'''
Input:
105201

Output:
894798


Input:
10000001

Output:
Wrong Input

replace 0 with 9 1 with 8 2 with 7 so on so forth
'''


n = int(input())
c1=c2=c0=0
while n:
    a=int(input())
    if a==1: c1+=1
    elif a==2:c2+=1
    else: c0+=1
    n-=1

result = [1]*c1+[0]*c0 +[2]*c2
print(*result)

'''
Input :
6
0
1
2
0
1
2

Output :

1 1 0 0 2 2

print all ones then zeros then twos
'''