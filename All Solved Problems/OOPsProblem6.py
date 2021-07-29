class Cake :
    def __init__(self,id, price, size, name):
        self.id =id;
        self.price = price
        self.size =  size
        self.name = name


class CakeShop :
    def __init__(self, cakeList,cakeShopName="BakersShop"):
        self.cakeShopName = cakeShopName
        self.cakeList = cakeList

    def findMinimumCakeBySize(self):
        if self.cakeList:
            resultcake = self.cakeList[0];
            for cake in self.cakeList:
                if cake.size < resultcake.size:
                    resultcake = cake
            return resultcake
        else:
             return None
    

    def sortCakeByPrice(self):
        if cakeList:
            return sorted(cakeList , key = lambda x: x.price)
        else:
            None

n =  int(input())
cakeList = []
while n:
    cid = int(input())
    price = int(input())
    size = int(input())
    name = input()
    C = Cake(cid, price, size, name)
    cakeList.append(C)
    n = n - 1
cshop = CakeShop(cakeList)
smallcake = cshop.findMinimumCakeBySize()
if smallcake:
    print(smallcake.id,smallcake.price,smallcake.size,smallcake.name,sep="\n")
else:
    print("No Data Found")
cakelistsorted = cshop.sortCakeByPrice()
if cakelistsorted:
    for cake in cakelistsorted:
        print(cake.price)
else:
    print("No Data Found")

'''
5
101
247
5
Black Forest Cake
102
877
8
Red Velvet Cake
103
319
4
Honey and Nut Cake
104
620
3
White Forest Cake
105
763
9
CheeseCake
'''            