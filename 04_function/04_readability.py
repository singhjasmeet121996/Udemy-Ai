price_p_ = 15

def calculate_bill(cup):
    cup = int(input("how many cups ordered: "))
    return cup * price_p_

bill = calculate_bill(4)

print(f"total bill is {bill}")