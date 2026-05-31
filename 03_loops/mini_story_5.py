# using zip method

name = ["a","b","c"]

amt = [10,10,30]

for name,amt in zip(name,amt):
    print(f"Bill amount for {name} is {amt}")
