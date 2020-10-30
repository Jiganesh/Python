def lcsa(str1,str2):

          lcs=[ [ [ ] for i in range(len(str1)+1)]  for j in range(len(str2)+1)]
          #Creating 2D matrix 

          for i in range (1,len(str1)+1):
                    for j in range (1,len(str2)+1):
                              #as we are using empty string in 0 and 0 index we have to add +1
                              

                              if str2[i-1]==str1[j-1]:
                                        lcs[i][j]= lcs[i-1][j-1]+ [str2[i-1]]
                                        
                              else:
                                        lcs[i][j]= max(lcs[i-1][j],lcs[i][j-1],key=len)
                                        
          return lcs[-1][-1]

print(lcsa("dsadsa","asadas"))

          
