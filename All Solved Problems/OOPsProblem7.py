class Passenger:
    def __init__(self, PassengerId, PassengerName , SeatNo, MealOpted, Class):
        self.PassengerId = PassengerId
        self.PassengerName = PassengerName
        self.SeatNo = SeatNo
        self.MealOpted = MealOpted
        self.Class = Class

class Airline:
    def __init__(self, plist, bmlist):
        self.plist = plist
        self.bmlist = bmlist 

    def getEconomyOrderedMealsCount(self):
        result  = {"EconomyMealsOrdered":0, "EconomyMealsNotOrdered":0}
        count = 0
        for i in self.plist:
            if i.Class.lower() == "economy":
                count+=1
                if i.MealOpted.lower() == "yes" :
                    count += 1
                    result["EconomyMealsOrdered"]+=1
                else:
                    result["EconomyMealsNotOrdered"]+=1
        return result if count > 0 else None

    def getBusinessOrderedMealsCount(self, seatnumber):
        for j in self.bmlist:
            for i in self.plist:
                if j.lower() == i.PassengerId.lower() and i.SeatNo.lower() ==seatnumber.lower():
                    return self.bmlist[j]
        else : 
            return None       

        
n = int(input())
plist = []
bmlist = {}
while n: 
    pid = int(input())
    pname = input()
    seatno = input()
    mealopt = input()
    Class = input()
    p = Passenger(pid, pname, seatno, mealopt, Class)
    plist.append(p)
    if Class == "business":
        bmlist[pid] = []

    n -= 1
menu = []
c = len(bmlist)*2
while c:
    menu.append(input())
    c -= 1
for i in bmlist:
    bmlist[i].append(menu[0])
    bmlist[i].append(menu[1])
    menu = menu[2:]
    
    
seatnumber = input()
airline = Airline(plist, bmlist)
emc = airline.getEconomyOrderedMealsCount()
if emc:
    for i in emc:
        print(i, emc[i],sep =":")
else :
    print("no passenger in economy class")
bmc = airline.getBusinessOrderedMealsCount(seatnumber)
if bmc:
    for i in bmc:
        print(i)
else:
    print("passenger does not belong to business class")

'''
// Testcase 1

5
101
pas1
21A
no
economy
102
pas2
7B
no
economy
103
pas3
2A
yes
business
104
pas4
3B
yes
business
105
pas5
21B
yes
economy
vegPulao
Ada Payasam
Lachcha Paratha
Veg Biryani
3B

//Testcase 2

4
101
pas1
1A
yes
business
2
pas2
4B
no
business
3
pas3
2A
yes
business
4
pas4
3B
yes
business
vegPulao
cheese sandwitch
chicken sandwhich
sewai payasam
Paneer Paratha
aloo paratha
idli sambar
cheese sandwhich
6B
'''