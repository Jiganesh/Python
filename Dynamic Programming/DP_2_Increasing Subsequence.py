def longestIncreasingSubsequence(array):

          sequences = [None for x in array]
          lengths=[1 for x in array]
          maxlengthidx=0

          for i in range (0,len(array)):
                    currentNum= array[i]
                    
                     for j in range (0,i):
                              otherNum = array[j]

                              if otherNum < currentNum and lengths[j]+1 >= lengths[i]:
                                        lengths[i] = lengths[j]+1
                                        sequences [i] = j
                                        
                    if lengths[i] >= lengths[maxlengthidx]:
                              maxlengthidx=i
                              
          return buildsequence(array,sequences, maxlengthidx)

def buildsequence(array,sequences,currentidx):
          seq=[]
          while currentidx   != None:
                     seq.append(array[currentidx])
                     currentidx=sequences[currentidx]
          return list(reversed(seq))

print(longestIncreasingSubsequence([5,7,-24,12,10,2,3,12,5,6,35]))
