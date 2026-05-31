def add_vat(p,vr):
    return p * (100+vr)/100

for pr in range(1,4):
    order_price = int(input(f"price of {pr} is: "))
    fp = add_vat(order_price,10)
    print(f"Final price for {pr} item is {fp}")