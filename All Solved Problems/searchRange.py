#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        pos=-1
        
        while l <=r:
            mid= l + (r-l) //2
            if nums[mid]==target:
                pos=mid
                break
            elif nums[mid]< target:
                l=mid+1
            else:
                r=mid-1
        i=j=pos
        if pos!=-1:
            while i >=0   and nums[i]==target:
                i-=1
            i+=1
            while j < len(nums) and nums[j]== target:
                j+=1
            return [i,j-1]
        else:
            return [-1,-1]

print(Solution().searchRange([3,3,3,4,5,6,6,6,6,7,8,8,8],6))
