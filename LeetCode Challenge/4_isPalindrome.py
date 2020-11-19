class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        return x==x[::-1] if abs(int(x))<2**31-1 else False

print(Solution().isPalindrome(-26348))
print(Solution().isPalindrome(2222))
