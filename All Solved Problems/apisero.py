def getBlocks(N,X,K,S):
  blocks = []
  i = 1
  for i in range(1, N+1):
    start, end = ((i-1) * X+1), min(N, (i*X))
    if start > N:
      break
 
    blocks.append(list(set(S[start-1:end])))
    blocks[-1].sort()
  return blocks

def Find_It(N, X, K, s):
    digits = getBlocks(N, X, K, s)
    freq = [len(x) for x in digits]
    for i in range(len(freq) - 2, -1, -1):
        freq[i] = freq[i] * freq[i + 1]
    if K > freq[0]:
        return -1
    freq.append(1)
    ans = []
    K = K - 1
    for i in range(1, len(freq)):
        div = K // freq[i]
        ans.append(digits[i - 1][div])
        K = K % freq[i]
    print(''.join(ans))
    

n ,x ,k = map(int,"10 5 10".split())
s = '1234567891'#input()

Find_It(n,x,k,s)
            
# Second Code From here

def profitMax(array):
    dpmatrix = [elements for elements in array]

    for i in range(0,len(array)):
        for j in range(0,i):
            if array[i]%array[j]==0:
                dpmatrix[i] = max(dpmatrix[i],dpmatrix[j]+array[i])
    return max(dpmatrix)
 
n = int(input())
array = [int(i) for i in input().split()]
print(profitMax(array))

    






