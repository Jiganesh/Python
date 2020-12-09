# https://leetcode.com/problems/majority-element/submissions/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = 0
        count = 1

        for i in nums:
            if majority_element == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority_element = i
                    count = 1
        return majority_element
