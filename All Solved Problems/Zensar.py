n = int(input())
while n:
    p=input()
    print(1 if len(set([p[i] for i in range(len(p)) if i%2==0]))==1 else 0)
    n-=1
    
'''

If all character at even places are same then there is virus else not

4
121&121
aba1a0*
12345
aaaaaaa

3
ADAOAS
MADAM
LFLRL
'''