class Solution(object):
    
    def generate(self, n):
        
        result= ""
        i=0
        
        while i < len(n):
            count=1
            while i+1 < len(n) and n[i]==n[i+1]:
                count+=1
                i+=1
            result += str(count)+n[i]
            i+=1
        return result
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        number="1"    
        for i in range (n-1):
            number= self.generate(number)
        return number