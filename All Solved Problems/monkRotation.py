# https://www.hackerearth.com/practice/codemonk/

n= int(input())
while n != 0:
    m,p = map(int,input().split())
    array = list(map(int, input().split()))
    p = p%m
    b = array[-p:]+array[:-p]
    print(*b)
    n-=1