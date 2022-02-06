n = input()
p = int(input())-1

output =[n]

while p:
    
    pointer = 0
    s =""
    while pointer<len(n):
        count = 0
        c = n[pointer]
        while pointer<len(n) and n[pointer]==c:
            count+=1
            pointer+=1
        s+=str(count)+c
        
    output.append(s)
    n =s
        
    p-=1  
    
print(*output, sep=",")      