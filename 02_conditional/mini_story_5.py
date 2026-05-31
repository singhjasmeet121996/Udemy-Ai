# Delivery fee remover using turnary opration

order_amt = float(input("Enter your order amount: "))

del_fee = 0 if order_amt > 300 else 30
print(f"Delivery fee is : {del_fee}")