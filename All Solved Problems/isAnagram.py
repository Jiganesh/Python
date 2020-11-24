#https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return {i: s.count(i) for i in s}=={i :t.count(i) for i in t}
