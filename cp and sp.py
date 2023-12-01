cost_price=int(input("enter the c price"))
selling_price=int(input("enter the s price"))
if cost_price>selling_price:
    loss=cost_price-selling_price
    print(loss)
elif selling_price>cost_price:
    profit=selling_price-cost_price
    print(profit)
else:
    print("no profit and no loss")




