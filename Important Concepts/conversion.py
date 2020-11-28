def binaryToDecimal(binary):

    binary = str(binary) 
    decimal = 0
    i=0
    n=len(binary)
    while i < n:
        decimal += int(binary[i]) * 2**(n-i-1)
        i+=1
    return decimal

def binaryToOctal(binary):
    binary=list(str(binary))
    
    while (len(binary))%3 !=0:
        binary.insert(0,"0")


    d= {"000":"0",
    "001":"1",
    "010":"2",
    "011":"3",
    "100":"4",
    "101":"5",
    "110":"6",
    "111":"7"
        }
    octal=""
    i=0
    while i+3 <=len(binary):
        block = "".join(binary[i:i+3])
        octal+= d[block]
        i+=3
    return octal



print(binaryToDecimal(1111))
print(binaryToOctal(110111100))