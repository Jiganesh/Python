class Apparel:
    def __init__(self , apparelbrand, type,price , instock):
        self.apparelbrand = apparelbrand
        self.type = type
        self.price = price
        self.instock = instock

    
class store :
    def __init__(self):
        self.apparelList = []

    def append (self, a):
        self.apparelList.append(a)


    def checkApparelAvailability(self, brand, type, apparelsize, numberofapperal):

        for i in self.apparelList:

            if i.apparelbrand == brand and i.type == type :

                if  apparelsize in i.instock and  i.instock[apparelsize]>numberofapperal:
                    print ("Size is Available")
                    i.instock[apparelsize]-=numberofapparel
                    for k , v in i.instock.items():
                        print(str(k)+":"+str(v))
                    return ""
                else:
                    print("Size not Available")
        return "Apperal not found"


n = int(input())
s = store()
while n:
    brand = input()
    typeof = input()
    price = int(input())
    instock ={}
    count = int(input())
    while count:
        apperalsize = input()
        apperalcount = int(input())
        instock[apperalsize]=apperalcount
        count-=1

    a = Apparel(brand , typeof , price, instock)
    s.append(a)
    n-=1


brandtofind = input()
typetofind = input()
aplsize = input()
numberofapparel = int(input())
print(s.checkApparelAvailability(brandtofind,typetofind,aplsize, numberofapparel))


'''
// TestCase 1
3
Van huessan
Shirt
1500
3
S
1
M
2
L
0
Louis Philip
Trousers
2800
2
S
2
M
2
India Terrain
Shorts
1000
3
S
3
M
7
L
2
Louis Philip
Trousers
M
1


// TestCase 2
3
Van huessan
Shirt
1500
3
S
1
M
2
L
0
Louis Philip
Trousers
2800
2
S
2
M
2
Indian Terrain
Shorts
1000
3
S
3
M
7
L
2
Louis Philip
Shirt
L
1
'''


