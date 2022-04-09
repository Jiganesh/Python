

class UserMainCode (object):
    @classmethod
    def majority(cls, input1, input2):
        
        '''
        input1 : int
        input2 : int[]
        '''
        
        # Read only region end
        # write code here
        
        d = [i for i in input2 if input2.count(i) > input1//2 ]
        
        return d[0] if d else -1
    
    
    
print(UserMainCode().majority(4,[1,2,1,2]))
print(UserMainCode().majority(3,[1,2,1]))



from itertools import combinations
class UserMainCode (object):
    @classmethod
    def minPenalty(cls, input1, input2):
        
        '''
        input1 : int
        input2 : int[]
        '''
        input2.sort()
        sum= 0
        for i in range (1 , input1):
            sum += min(abs(input2[i-1] - input2[i]), abs(input2[i]-input2[i-1]))
        return sum
    
print(UserMainCode().minPenalty(4,[1,6,-2,4]))
print(UserMainCode().minPenalty(3, [1,3,2]))
