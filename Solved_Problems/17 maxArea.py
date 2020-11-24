# https://leetcode.com/problems/container-with-most-water/submissions/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=maxarea=0
        j=len(height)-1
        while i < j :
            maxarea = max (maxarea, min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            elif height[j] < height[i]:
                j-=1
            else:
                i+=1
                j-=1
        return maxarea

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
