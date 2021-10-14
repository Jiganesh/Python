word  = input().split()
n = int(input())
print(len([i for i in word if i==i[::-1]]))