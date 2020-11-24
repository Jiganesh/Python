#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range (len(num)):
                current_num = num[i]

                if target-current_num in d:
                        return [d[target-current_num],i]

                d[current_num]=i
