

def groupDigits(number, delimiter):
    string = str(number)
    if len(string) <4:
        return string
    else: 
        last = [string[-3:]]
        string = string[:-3]
        other=[]
        while string:
            other.append(string[-2:])
            string = string[:-2]
        return delimiter.join(other[::-1]+last)

# string = input()
# delimiter = input()
# print(groupDigits(string, delimiter))

print(groupDigits(100000,"#"))
print(groupDigits(756,","))