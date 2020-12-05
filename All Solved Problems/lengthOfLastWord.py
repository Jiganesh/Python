#https://leetcode.com/problems/length-of-last-word/submissions/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        length = len(s)-1
        count = 0

        while length >= 0:
            if s[length] == " ":
                break
            count += 1
            length -= 1
        return count
