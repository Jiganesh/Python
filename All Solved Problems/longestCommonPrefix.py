# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    
    def find(self , s1, s2):
        n1=len(s1)
        n2=len(s2)
        i=j=0
        result=""
        while i <n1 and j <n2:
            if s1[i]!=s2[j]:
                break
                
            result+=s1[i]
            i+=1
            j+=1
        return result
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0] if strs!=[] else ""
        for i in strs:
            result = Solution().find(result, i)
        return result
