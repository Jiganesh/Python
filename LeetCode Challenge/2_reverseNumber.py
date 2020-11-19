class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=0
        flag = -1 if x<0 else 1
        x=abs(x)
        while x>0:
            ans= ans*10 + x%10
            x//=10
        return 0 if abs(ans)>= (2**31)-1 else flag*ans    
        
        # The largest 32 bit number is not 2^32 cause we need 1 bit to reserve sign bit
        # Hence 2**32 - 1
                

print(Solution().reverse(321))
print(Solution().reverse(-348))
print(Solution().reverse(0))

