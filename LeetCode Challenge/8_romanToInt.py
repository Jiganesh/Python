class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d= {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res=i=0
        while i < len(s):
                curr_roman = s[i]
                if i+1 < len(s):
                        if d[curr_roman] >= d[s[i+1]]:
                                res+= d[curr_roman]
                                i+=1
                        else:
                                res+= d[s[i+1]]-d[curr_roman]
                                i+=2
                else:
                        res+=d[curr_roman]
                        i+=1
        return res

print(Solution().romanToInt("III"))