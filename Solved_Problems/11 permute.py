class Solution(object):
    def heapPermutation(self, a, size, n,res):
 
        if (size == 1):
            res.append(tuple(a))


        for i in range(size):
            Solution().heapPermutation(a, size-1, n,res)
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]

        return res

        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        return [list(i) for i in self.heapPermutation(nums,n,n,[])]

print(Solution().permute([1,2,3]))