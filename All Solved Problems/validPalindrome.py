#https://leetcode.com/problems/valid-palindrome/submissions/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_of_char = [i.lower() for i in s if i.isalnum()]
        return list_of_char == list_of_char[::-1]
