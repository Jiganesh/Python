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
                

print(twoSum([3,2,4],6))
print(twoSum([2,7,11,15],9))
print(twoSum([3,3],6))

                
