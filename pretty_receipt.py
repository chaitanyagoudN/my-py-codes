from datetime import datetime as dt
from importlib.metadata import packages_distributions
thisdict={}
count=0
catList=[]
user_1={}

while(True):
    user=int(input("for category - enter 1 to go else exits"))
    if user==1 :
        cat=str(input("enter the cat name: "))
        dict1={}
        while(True):
            subcat=int(input("for product - name enter 1 to go else exits"))
            if subcat == 1:
                set={}
                product_name=str(input("enter the product name :"))
                price=float(input("enter the price :"))
                dict1[product_name]=price
            else:
                thisdict[cat]=dict1
                break   
    else:
        print(thisdict)
        break

for catogery in thisdict:
    print(catogery)
    for products in thisdict[catogery]:
        print("     ",products, thisdict[catogery][products])

while(True):
    x=int(input("If you want to purchase a porduct enter 1, else 0: "))
    if x==1 :
        pname=input("Enter product name :")
        quantity=int(input("enter quantity for product :"))
        user_1[pname]=quantity
    else:
        break

categorylist=[]
for catogery in thisdict:
    categorylist.append(catogery)

categorylist.sort()
print(categorylist)

tl=()
full_orders={}
total=0

for cat in categorylist:
    for catogery in thisdict:
        if cat==catogery:
            orders=[]
            for products in thisdict[catogery]:
                for choice in user_1:
                    if choice==products:
                        order=[]
                        subprice=thisdict[catogery][products]*user_1[choice]
                        total+=subprice
                        order.append(choice)
                        order.append(subprice)
                        order.append(user_1[choice])
                        orders.append(order)
            full_orders[catogery]=orders

print(full_orders)
titems=0
for choice in user_1:
    titems=titems+user_1[choice]

print("*************RECIEPT************")
x = dt.now()
print(x.strftime("%m/%d/%Y %H:%M %p"))
bar="**********************************"
print(bar)
print("Total Items:",'{:15}'.format(titems))
print(bar)
print('{:2} {:2} {:10} {:4}'.format("Cat", "Product","Quantity","price"))
for cat in full_orders:
    print(cat)
    for prodlist in full_orders[cat]:
            print("     ",'{:10} {:3} {:5}'.format(prodlist[0],prodlist[2],prodlist[1]))
print("Subtotal",'{:19}'.format(total))
taxs=round(total*(15/100))

print("Tax",'{:20}'.format(taxs))
print(bar)
print("Total",'{:21}'.format(total+taxs))
cashpaid=int(input(" Enter the  cashpaid "))
print("cashPaid",'{:22}'.format(cashpaid))
print(bar)
print("Change",'{:18}'.format(cashpaid-(total+taxs)))

