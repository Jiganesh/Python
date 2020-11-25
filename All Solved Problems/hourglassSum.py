# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def hourglassSum(array):
    row= len(array)
    column = len(array[0])
    ans=-999999
    
    for i in range (row-2):
        for j in range (column-2):
            top = array[i][j]+array[i][j+1]+array[i][j+2]
            mid = array[i+1][j+1]
            bottom = array[i+2][j]+array[i+2][j+1]+array[i+2][j+2]
            summation= top+mid+bottom
            ans=max(ans,summation)
    return ans
    