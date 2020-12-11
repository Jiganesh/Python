# https://leetcode.com/problems/maximum-subarray/submissions/

# Kadane's Algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = largest = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            largest = max(largest, curr)

        return largest
