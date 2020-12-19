# https://codeforces.com/problemset/problem/791/A
# Code Fores Easy Problems

m,n = map(int , input().split())
count=0
while m <=n:
        m,n = 3*m, 2*n
        count+=1
print(count)