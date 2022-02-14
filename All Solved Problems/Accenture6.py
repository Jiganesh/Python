
input1 = "phqgh"
a = sorted(set(list(input1)))
print( "".join([i + str(input1.count(i)) for i in a]))
        

                