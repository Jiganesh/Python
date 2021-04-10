# exam of mink problem

class players:
    def __init__(self, playerName, playedCountry, playerAge, countryFrom):

        self.playerName = playerName
        self.playedCountry = playedCountry
        self.playerAge = playerAge
        self.countryFrom = countryFrom



def countplayers(listofPlayers, country):
    count = 0

    for i in listofPlayers:
        if i.countryFrom.lower()== country.lower():
            count+=1

    return count


def getPlayerPlayedForMaxCountry(listofPlayers):

    maxplayer =""
    currentmax =0
    for i in listofPlayers:
        if currentmax < len(i.playedCountry):
            currentmax = len(i.playedCountry)
            maxplayer = i.playerName
    
    return maxplayer



n = int(input())
allplayers =[]

while n :
    name = input()
    cp = int(input())
    array=[]
    while cp:
        array.append(input())
        cp-=1
    playerage = int(input())
    countryfrom = input()



    object = players(name,array,playerage,countryfrom)
    allplayers.append(object)
    n-=1

argument = input()

print(countplayers(allplayers,argument))
print(getPlayerPlayedForMaxCountry(allplayers))











'''
5
Rahul
5
Japan
Brazil
Chaina
Nepal
India
40
India
Kamini
4
Denmark
Australia
Indonesia
Ghana
37
India
Sunil
6
Brazil
Bhutan
Afghanistan
UK
Nepal
Newzeland
32
India
Ricky
3
Australia
Europe
Germany 
42
UK
Ramij
2
Pakistan
Bhutan
39
Pakistan
India
'''