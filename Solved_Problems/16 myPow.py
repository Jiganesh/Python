class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n <0:
            x=(1/x)
        return x** abs(n)
print(Solution().myPow(2.0000,-2))
print(Solution().myPow(2.0000, 2))
