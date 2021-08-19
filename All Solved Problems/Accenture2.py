def SumOfPro(arr1, arr2):
    sum = 0
    for i in range (len(arr1)):
        sum +=(arr1[i]* arr2[len(arr1)-i-1])
    return sum

print(SumOfPro([22,7,1,5,5,-2],[4,-1,21,12,10,-3]))


# implement the function that find and return the minimum characters required to append at the end of str to make it palindrome





def convertToPalindrome(str):
    for i in range( len(str)): 
        if str[-1]==str[i]:
            return str[:i][::-1]







print(convertToPalindrome("abcdc"))
print(convertToPalindrome("abcde"))
