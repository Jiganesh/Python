class UserMainCode(object):
    def lengthOfLIS(cls, input1, input2):
        
        if not input2:
            return 0
        
        dp = [1] * input1

        for i in range(1, input1):
            for j in range(i):
                if input2[i] > input2[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)