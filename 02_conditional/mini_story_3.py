#  Chai Price Calulator

cup_size = input("what size would you like to order:").lower()

if cup_size == "small":
    print(f"this will cost you 10 rupees")
elif cup_size == "medium":
    print(f"this will cost you 15 rupees")
elif cup_size == "large":
    print(f"this will cost you 20 rupees")
else:
    print(f"sorry we don't do that size")

