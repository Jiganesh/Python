# https://codeforces.com/contest/1609/problem/A

'''
William has array of n numbers a1,a2,…,an. He can perform the following sequence of operations any number of times:

Pick any two items from array ai and aj, where ai must be a multiple of 2
ai=ai2
aj=aj⋅2
Help William find the maximal sum of array elements, which he can get by performing the sequence of operations described above.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). Description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤15), the number of elements in William's array.

The second line contains n integers a1,a2,…,an (1≤ai<16), the contents of William's array.

Output
For each test case output the maximal sum of array elements after performing an optimal sequence of operations.

5
3
6 4 2
5
1 2 3 4 5
1
10
3
2 3 4
15
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
outputCopy
50
46
10
26
35184372088846
Note
In the first example test case the optimal sequence would be:

Pick i=2 and j=1. After performing a sequence of operations a2=42=2 and a1=6⋅2=12, making the array look as: [12, 2, 2].
Pick i=2 and j=1. After performing a sequence of operations a2=22=1 and a1=12⋅2=24, making the array look as: [24, 1, 2].
Pick i=3 and j=1. After performing a sequence of operations a3=22=1 and a1=24⋅2=48, making the array look as: [48, 1, 1].
The final answer 48+1+1=50.

In the third example test case there is no way to change the sum of elements, so the answer is 10.
'''

n = int(input())
while n :
    s,m =-1,1
    t = int(input())
    array = list(map(int, input().split()))
    for i in array:
        if i%2==0:s+=1;m*=i
        else: s+=i
    print(s+m)