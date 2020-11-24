# https://leetcode.com/problems/integer-to-roman/submissions/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numbers= [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        symbols= ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        s=""
        i=12
        while num:
            div = num // numbers[i]
            num = num%numbers[i]
            
            while div:
                s+=symbols[i]
                div-=1
            i-=1
        return s
    