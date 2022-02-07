
def maxNumberArray(number1, number2, givenlength):

	len1, len2 = len(number1), len(number2)
	result = []

	def helper(nums, c_len):
		answer = []
		lenOfNums = len(nums)
		for index, value in enumerate(nums):
			while answer and answer[-1] < value and lenOfNums-index > c_len-len(answer):
				answer.pop(-1)
			if len(answer) < c_len:
				answer.append(value)
		return answer

	for s1 in range(max(0, givenlength-len2), min(givenlength, len1)+1):
		p1, p2 = helper(number1, s1), helper(number2, givenlength-s1)
		result = max(result, [max(p1, p2).pop(0) for _ in range(givenlength) if max(p1,p2)])
	return result

arr1 = list(map(int, input().split(",")))
arr2 = list(map(int, input().split(",")))

givenlength = int(input())

print(*maxNumberArray(arr1, arr2, givenlength), sep=",")


"""
3,8,4,5
9,1,2,6,7
5
"""
