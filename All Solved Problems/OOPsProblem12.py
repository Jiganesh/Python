class Product :
    def __init__(self, pid, pbrand, ptype, unitprice, qinhand, status="Available"):
        self.pid = pid
        self.pbrand = pbrand
        self.ptype = ptype
        self.unitprice = unitprice
        self.qinhand = qinhand
        self.status = status
        
class shippingCompany:
    def __init__(self, listofproducts, shippingchargelist):
        self.listofproducts = listofproducts
        self.shippingchargelist = shippingchargelist
        
        # shippingchargelist = {city : shippingcharge}
        
    def shippingbill(self, pbrand, ptype, city, quantity):
        
        for i in self.listofproducts:
            if i.pbrand == pbrand and i.ptype == ptype and city in self.shippingchargelist:
                if i.qinhand >= quantity:
                    i.qinhand -= quantity
                    
                    if i.qinhand<=0:
                        i.status = "Unavailable"
                    return i.unitprice*quantity + self.shippingchargelist[city]*quantity
        return None
    
    def producttypewisecount (self):
        array = []
        for i in self.listofproducts:
            if i.qinhand>0: array.append(i.ptype)
            
        return {i : array.count(i) for i in set(array)}
    
    
n = int(input())
listofproducts =[]
while n :
    pid = int(input())
    pbrand= input().lower()
    ptype = input().lower()
    unitprice = int(input())
    qinhand = int(input())
    listofproducts.append(Product(pid, pbrand, ptype, unitprice, qinhand))
    n-=1
            
m = int(input())
shippingCharge ={}
while  m :
    city = input().lower()
    price = int(input())
    shippingCharge[city] = price
    m-=1
    
productbrand = input().lower()
producttype = input().lower()
productcity = input().lower()
productquantity = int(input())  

ShippingCompany = shippingCompany(listofproducts, shippingCharge)
amount  = (ShippingCompany.shippingbill(productbrand, producttype, productcity, productquantity))
dictionary = (ShippingCompany.producttypewisecount())


if amount :
    print("Bill Calculated:" + str(amount))
else:
    print("Product Not Found")
    
if dictionary:
    for i in sorted(dictionary.keys()):
        print(i.title() + " " + str(dictionary[i]))
else:
    print("No Products Found")

"""
5
1011
Leo
Electronic
300
20
1012
Ledo
Electronic
350
50
1021
Leo
Puzzle
100
20
2022
Leo
mechanics
400
30
1023
FunckCool
puzzle
350
20
3
Guwahati
50
Kolkata
30
Shillong
100
Leo
Electronic
Shillong
20

5
1011
Leo
Electronic
300
20
1012
Ledo
Electronic
350
50
1021
Leo
Puzzle
100
20
1022
Leo
mechanics
400
30
1023
FunkCool
puzzle
350
20
3
Guwahati
50
Kolkata
30
Shillong
100
Leo
Electronic
Delhi
20

"""
    
    