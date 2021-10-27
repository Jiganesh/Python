class Order :
    def __init__(self, id, name, price, mode, order_date, delivered):
        self.id = id
        self.name = name
        self.price = price
        self.mode = mode
        self.order_date = order_date
        self.delivered = delivered
        
class Store :
    def __init__(self, list_of_orders):
        self.list_of_orders = list_of_orders
        
    def monthly_price(self, month):
        summation =0
        for i in self.list_of_orders:
            if int(i.order_date.split("-")[1]) == month and i.delivered.lower() == "yes" and "VanHeusen Shirt" in i.name:
                summation += i.price
        return summation if summation else None
    
    def dictionary_key(self, price):
        d ={}
        for i in self.list_of_orders:
            if i.price >= price:
                if i.mode in d:
                    d[i.mode] += 1
                else:
                    d[i.mode] = 1  
                
        return d if d else None

n = int(input())
list_of_orders = []
while n:
    orderid = int(input())
    m = int(input())
    ordername =[]
    while m:
        ordername.append(input())
        m-=1
    orderprice = float(input())
    ordermode = input()
    orderdate = input()
    orderdelivered = input()
    list_of_orders.append(Order(orderid, ordername, orderprice, ordermode, orderdate, orderdelivered))
    n -= 1
    
month = int(input())
price = float(input())
store = Store(list_of_orders)
total=store.monthly_price(month)
print(total if total else "No order delivered with given criteria")

d = store.dictionary_key(price)
if d: 
    for i in d:
        print(i, d[i])
else : 
    print("No order found with given criteria")


'''
5
101
2
Almonds
VanHeusen Shirt
250.5
Net Banking
12-03-2021
yes
102
4
VanHeusen Shirt
1 kg Rice
Tata Tea
2 kg Sugar
550.50
COD
22-03-2021
yes
103
2
Ashirvad Aata
1 kg sugar
150.15
Credit Card
12-08-2021
yes
104
3
VanHeusan Shirt
1 kg sona masoori
2 kg chana
1550.50
COD
15-03-2021
yes
105
4
curd
tomatoes
milk
potatoes
150.50
Net Banking
22-07-2021
yes
3
1600


5
101
2
Almonds
Walnut
250.5
Net Banking
12-03-2021
yes
102
4
VanHeusan Pant
1 kg Moong
Tata Tead
2 kg Sugar
550.50
COD
22-03-2021
no
103
2
Ashirvad Aata
1 kg sugar
150.15
Credit Card
12-08-2021
yes
104
3
VanHeusan Shirt
1 kg sona masoori
2 kg chana
1250.50
COD
15-03-2021
no
105
4
curd
tomatoes
milk
potatoes
150.50
Net Banking
22-07-2021
yes
7
100

'''