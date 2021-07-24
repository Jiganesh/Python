class Food:
    def __init__(self,name, proteins, fat, carbohydrates, energy=0, status=""):
        self.name = name
        self.proteins=proteins
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.energy = energy
        self.status = status

class Nutrition:
    def __init__(self, energydict, foodList):
        self.energydict = energydict
        self.foodList = foodList

    def  setEnergy(self):
        for i in self.foodList:
            i.energy = i.fat + i.proteins + i.carbohydrates
            for p in self.energydict:
                name = p
                tupled = self.energydict[p]
                lower = tupled[0]
                upper = tupled[1]
                if i.energy >= lower and i.energy <= upper:
                    i.status = name
                    
        return foodList

    def getEnergy(self, value):
        Listlessvalue =[]
        for i in self.foodList:
            if i.energy<= value:
                Listlessvalue.append(i)
        
        return Listlessvalue
    
n = int(input())
foodList =[]
while n:
    name = input()
    protein = float(input())
    fat = float(input())
    carbohydrate = float(input())
    item =Food(name, protein, fat, carbohydrate)
    foodList.append(item)
    n -= 1

p =int(input())
dictionary = {}
while p:
    key =input()
    num1 = int(input())
    num2 =int(input())
    dictionary[key] = (min(num1,num2),max(num1,num2))
    p-=1


nutritionobj = Nutrition(dictionary, foodList)

value =int(input())
itemlist = nutritionobj.setEnergy()
print("Energy of Food :")
for i in itemlist :
    print(i.name, i.energy, i.status, sep="-")

listlessvalue = nutritionobj.getEnergy(value)
if listlessvalue:
    print ("Food within given criteria:")
    for i in listlessvalue:
        print(i.name+":"+str(i.energy))
else:
    print("No Food Found")


    
'''
5
Apple
2.0
1.0
25.1
Beans
10.5
5.0
6.5
Meat
41.5
44.5
56.0
Milk
35.5
41.4
45.0
Chocolate
10.0
30.5
35.0
4
Low
0
50
Medium
51
100
High
101
150
Very High
151
200
40


'''