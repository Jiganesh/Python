def binaryToDecimal(binary):

    binary = str(binary)
    decimal = 0
    i = 0
    n = len(binary)
    while i < n:
        decimal += int(binary[i]) * 2**(n-i-1)
        i += 1
    return decimal


def binaryToOctal(binary):
    binary = list(str(binary))

    while (len(binary)) % 3 != 0:
        binary.insert(0, "0")

    d = {"000": "0",
         "001": "1",
         "010": "2",
         "011": "3",
         "100": "4",
         "101": "5",
         "110": "6",
         "111": "7"
         }
    
    octal = ""
    i = 0
    while i+3 <= len(binary):
        block = "".join(binary[i:i+3])
        octal += d[block]
        i += 3
    return octal


def binaryToHexadecimal(binary):
    binary = list(str(binary))

    while (len(binary)) % 4 != 0:
        binary.insert(0, "0")

    d = {"0000": "0",
         "0001": "1",
         "0010": "2",
         "0011": "3",
         "0100": "4",
         "0101": "5",
         "0110": "6",
         "0111": "7",
         "1000": "8",
         "1001": "9",
         "1010": "A",
         "1100": "B",
         "1101": "C",
         "1110": "D",
         "1111": "E"
         }

    hexadecimal = ""
    i = 0
    while i+4 <= len(binary):
        block = "".join(binary[i:i+4])
        hexadecimal += d[block]
        i += 4
    return hexadecimal


print(binaryToDecimal(1111))
print(binaryToOctal(110111100))
print(binaryToHexadecimal(11))
