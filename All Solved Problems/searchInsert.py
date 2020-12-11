# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """       
        # Linear Search
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
        return n
        """
        # Binary Search
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        else:
            return r+1
