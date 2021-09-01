
# Python3 program to get minimum lines to cover
# all the points
 
# Utility method to get gcd of a and b
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
 
# method returns reduced form of dy/dx as a pair
def getReducedForm(dy, dx):
    g = gcd(abs(dy), abs(dx))
 
    # get sign of result
    sign = (dy < 0) ^ (dx < 0)
 
    if (sign):
        return (-abs(dy) // g, abs(dx) // g)
    else:
        return (abs(dy) // g, abs(dx) // g)
    
def minLinesToCoverPoints(points, N, xO, yO):
    st = dict()
    minLines = 0
    for i in range(N):
        curX = points[i][0]
        curY = points[i][1]
 
        temp = getReducedForm(curY - yO, curX - xO)
        if (temp not in st):
            st[temp] = 1
            minLines += 1
 
    return minLines
 
n, m = int(input()), int(input())
 
points= [list(map(int, input().split())) for _ in range(n)]
x= int(input())
y= int(input())
N = len(points)
print(minLinesToCoverPoints(points, N, x, y))