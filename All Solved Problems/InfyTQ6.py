def fls(arr, n):

	s ,ans= set(arr), 0
	
	for i in range(n):
		if (arr[i]-1) not in s:
			j = arr[i]
			while(j in s): j += 1
			ans = max(ans, j-arr[i])
	return ans if ans>1 else -1

arr = list (map(int, input().split(",")))
print (fls(arr, len(arr)))

"""
36,41,56,35,44,33,34,92,43,32,42
-1,2,5,7
"""

