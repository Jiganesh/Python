#https://leetcode.com/problems/longest-palindrome/

class Solution(object):

    def getpalindrome(self,s,leftidx,rightidx):
        while leftidx>=0 and rightidx < len(s):
            if s[leftidx]!=s[rightidx]:
                break
            leftidx-=1
            rightidx+=1
        return [leftidx+1,rightidx]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        current=[0,1]
        for i in range (len(s)):
            even=Solution().getpalindrome(s,i-1,i)
            odd=Solution().getpalindrome(s,i-1,i+1)
            longest= max(even,odd,key=lambda l: l[1]-l[0])
            current= max(current,longest, key=lambda l: l[1]-l[0])
            
        return s[current[0]:current[1]]

