str1,str2 = input(), input()
i=count=0
while i < len(str1) or i< len(str2):
    if i< len(str1) and  i< len(str2) and str1[i]!= str2[i]:
        count+=1;
    i+=1
print(count + abs(len(str1)-len(str2)))
        