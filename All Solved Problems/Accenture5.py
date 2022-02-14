class UserMainCode(object):
    @classmethod
    def checkConsecutive(cls, input1, input2):
        
        arr = sorted(input2)
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != 1:
                return 0
        return 1
    
    
    
    
    