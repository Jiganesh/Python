import heapq
k=4
array = [10,5,3,6,7]
heapq.heapify(array)


for i in range(k):
    kth = heapq.heappop(array)
print(kth)
