class Solution(object):
    def backtracking (self, output_array, current_string , count_open ,count_close , n):
        
        if len(current_string)==n*2:
            output_array.append(current_string)
            return
        if count_open < n:
            self.backtracking(output_array,current_string+"(",count_open+1,count_close, n )
        if count_close < count_open:
            self.backtracking(output_array,current_string+")",count_open,count_close+1, n )
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """  
        output_array= []
        current_string =""
        self.backtracking(output_array,current_string,0,0, n )
        return output_array

print(Solution().generateParenthesis(3))
