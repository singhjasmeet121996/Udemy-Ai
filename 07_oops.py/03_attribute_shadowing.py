class Chai:
    temp = "hot"
    strenth = "Strong"

cutting = Chai()
print(cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("After changing temp",cutting.temp)
print(f"cup size for cutting is",cutting.cup)
print("Direct look into class",Chai.temp)


del cutting.temp
print(cutting.temp)
