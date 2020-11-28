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


def decimalToOctal(decimal):

    d = {"0": "000",
         "1": "001",
         "2": "010",
         "3": "011",
         "4": "100",
         "5": "101",
         "6": "110",
         "7": "111",
         }
    octal = ""
    for i in str(decimal):
        octal += d[i]
    return octal


def decimalToHexadecimal(decimal):

    d = {"0": "0000",
         "1": "0001",
         "2": "0010",
         "3": "0011",
         "4": "0100",
         "5": "0101",
         "6": "0110",
         "7": "0111",
         "8": "1000",
         "9": "1001",
         "A": "1010",
         "B": "1100",
         "C": "1101",
         "D": "1110",
         "E": "1111"
         }
    hexadecimal = ""
    for i in str(decimal):
        hexadecimal += d[i]
    return hexadecimal

def hexadecimalToOctal(hexa):
    


print(binaryToDecimal(00100011))
print(binaryToOctal(00100011))
print(binaryToHexadecimal(00100011))
print(decimalToOctal(23))
print(decimalToHexadecimal(23))
