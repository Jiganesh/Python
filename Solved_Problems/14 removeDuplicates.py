class Solution(object):
    def removeDuplicates(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j =0,1
        while j < len(array):
            if array[i]!=array[j]:
                i=i+1
                array[i]=array[j]
            j+=1
        return i+1
