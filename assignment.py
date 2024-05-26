
print("----------welcome to liquor mart---------------")

amount=0.0
statement=""
item_count=0
total_amount=0
while(True):
    price=int(input("Enter the cost: "))
    if price>0:  
        item_count=item_count+1
        amount=amount+(price)
    elif price==0:
        print("this is special perk item")
    else:
       break

if item_count>5:
    discount=(amount*(5/100))
    total_amount=amount-discount
    total_amount=total_amount+(total_amount*(6.5/100))
    print("Discounted amount :",discount)
    print("total amount without tax and discount:",amount)
    print("Items are more than 5, total amount after discount:",total_amount)

else:
    total_amount=amount
    print("Items are less than 5, total amount :",total_amount)
print("----------Thank you visit again!!!!--------------")