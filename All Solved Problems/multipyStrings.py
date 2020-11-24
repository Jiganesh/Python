# https://leetcode.com/problems/multiply-strings/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lista = [i for i in '0123456789']
        a= list(range (0,10))
        d= dict(zip(lista,a))
        d2=dict(zip(a,lista))
        n1=0
        for i in num1:
                n1=n1*10+d[i]
        n2=0
        for i in num2:
                n2=n2*10+d[i]
        
        ans= n1*n2
        a=[]
        while ans > 0 :
                a.append(ans%10)
                ans=ans//10
        a=a[::-1]
        return "".join([d2[i] for i in a]) if len(a)>0 else "0"
