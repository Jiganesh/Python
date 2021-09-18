n = int(input())
array = list(map(int, input().split(",")))
sumation = sum([ 1/i for i in array])
print("{:.2f}".format(1/sumation,2))
