class Boutique:

    def __init__(self, boutiqueid, boutiquename, boutiquetype, boutiquerating, points):
        self.boutiqueid = boutiqueid
        self.boutiquename= boutiquename
        self.boutiquetype= boutiquetype
        self.boutiquerating=boutiquerating
        self.points= points


class OnlineBoutique():

    def __init__(self,boutiqueDict):
        self.boutiqueDict=boutiqueDict

    def getboutique(self, llr, ulr, extrapoints, type):
        result = []
        if type.lower() in boutiqueDict.keys():
            for i in self.boutiqueDict[type.lower()]:

                if llr<=i.boutiquerating <=ulr:
                    i.points= int(i.points) + int(extrapoints)
                result.append(i)
        return sorted(result, key = lambda i :i.points)[::-1]
                


n = int(input())
boutiqueDict={}

while n:
    boutiqueid= int(input())
    boutiquename=input()
    boutiquetype=input().lower()
    boutiquerating=float(input())
    points= int(input())

    B = Boutique(boutiqueid, boutiquename, boutiquetype, boutiquerating, points)

    if boutiquetype.lower() in boutiqueDict:
        boutiqueDict[boutiquetype].append(B)
    else:
        boutiqueDict[boutiquetype]=[B]
    n-=1

llr = float(input())
ulr = float(input())
extrapoints =int(input())
boutiquetype =input()

O = OnlineBoutique(boutiqueDict)
result = O.getboutique(llr,ulr,extrapoints,boutiquetype)
output =[]
if result:
    for i in result:
        print(i.boutiqueid,i.boutiquename,i.points)

else:
    print("No boutique found")

'''
// TestCase 1

5
100
Olivia
Clothing
4.0
90
101
Little Lady
Kids
4.5
150
102
Ever After
Clothing
4.1
110
103
Fresh From Heaven
Flowers
4.3
120
104
Temple Designs
Designer Wear
3.6
80
4.0
5.0
50
Clothing

// TestCase 2

5
100
Olivia
Clothing
4.0
90
101
Little Lady
Kids
4.5
150
102
Ever After
Clothing
4.1
110
103
Fresh From Heaven
Flowers
4.3
120
104
Temple Designs
Designer Wear
3.6
80
4.0
5.0
50
Fashion
'''
