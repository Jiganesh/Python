repository = ["mobile", "mouse", "moneyPot", "monitor", "mousePad"]
customerQuery = "mouse"

repository.sort()
pointerInString =0;
result =[]

while (pointerInString != len(customerQuery)+1):
    pointerInArray = 0;
    currentString = customerQuery[:pointerInString]
    if len(currentString)>=2:
        while currentString not in repository[pointerInArray]:
            pointerInArray+=1
            if pointerInArray == len(repository):
                break
        result.append(repository[pointerInArray:])
    pointerInString+=1

for i in result:
    print(i[:3])
    
    