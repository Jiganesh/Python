class Product:
    def __init__(self , productname, producttype, productprice , quantityonhand, reorderingquantity):
        self. productname = productname
        self.producttype= producttype
        self.productprice = productprice
        self.quantityonhand = quantityonhand
        self.reorderingquantity = reorderingquantity


def findAvailableStock (listofproducts , listofproductnames):
    dictionary ={}
    for i in listofproducts:
        if i.productname in listofproductnames:
            dictionary[i.productname.lower()]=i.quantityonhand 

    
    return dictionary if dictionary !={} else  None # {productname : quantityonhand}

def updatestockbyproducttype(listofproducts, quantityadded , producttype):
    flag = False
    for i in listofproducts:
        if i.producttype == producttype :
            if i.quantityonhand < i.reorderingquantity:
                flag = True
                i.quantityonhand+=quantityadded

    return listofproducts if flag else None


n = 5
listofproducts=[]
while n :
    name =input()
    typeofp =input()
    price = int(input())
    quantityonhand = int(input())
    reorderingquantity = int(input())
    p = Product(name, typeofp, price, quantityonhand, reorderingquantity)
    listofproducts.append(p)
    n-=1

listofproductnames=[]
m = int(input())
while m:
    listofproductnames.append(input())
    m-=1

newnumber =int(input())
typeofproduct =input()

d=findAvailableStock(listofproducts,listofproductnames)
if d != None:
    for i in listofproductnames:
        if i.lower() in d:
            print(i +" "+ str(d[i.lower()]))
else:
    print("Product not Found")

v = updatestockbyproducttype(listofproducts, newnumber, typeofproduct)

if v != None:
    for i in v:
        print(i.productname, i.quantityonhand)
else:
    print("Product not Found")





'''
// Testcase 1
Pen
Stationary
25
30
5
Pencil
Stationary
20
20
10
Soap
Body care
15
100
30
Face Cream
Cosmetics
200
10
15
Shampoo
Body care
100
10
15
3
Soap
face cream
pen
20
Body care

//Testcase 2
Pen
Stationary
25
30
5
Pencil
Stationary
20
20
10
Soap
Body care
15
100
30
Face Cream
Cosmetics
200
10
15
Shampoo
Body care
100
10
15
3
Biscuit
Nail polish
Face Wash
20
Grossary
'''