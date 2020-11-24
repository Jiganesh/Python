#https://leetcode.com/problems/longest-common-subsequence/submissions/
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        text1+= " "*abs(len(text1) - len(text2))
        text2+= " "*abs(len(text1) - len(text2))
        
        lcs = [[[] for i in range (len(text1)+1)] for j in range (len(text2)+1)]
        
        for i in range (1,len(text1)+1):
            for j in range (1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    lcs[i][j]=lcs[i-1][j-1]+[text2[j-1]]
                else:
                    lcs[i][j]= max(lcs[i-1][j],lcs[i][j-1],key= len)
        a=[i for i in lcs[-1][-1] if i !=" "]
        return len(a)

print(Solution().longestCommonSubsequence("vaibhavi","jiganesh"))
