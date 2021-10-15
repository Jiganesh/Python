# # Calculate the century I/P : 1900, 2100
# n = int(input())
# print(n//100 if n%100==0 else n//100+1)


s = input()
n = int(input())
print(sorted([i for i in s if s.count(i)>=n])[0])


'''
I/P 

aaabbbkkkkdddd op d
bcabca op a

'''