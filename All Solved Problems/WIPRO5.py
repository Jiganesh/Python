# n = int(input())
# array = list(map(int,input().split()))
# a = [i for i in array if array.count(i)==i]

# print(max(a)if a else -1)
 
print(sum([int(i) for i in str(input()) if int(i)%2==0]))