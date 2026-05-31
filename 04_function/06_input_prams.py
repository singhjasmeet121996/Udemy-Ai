chai = "latte"

def prep_chai(order):
    print("Preparing", order)

prep_chai(chai)

print(chai)

def make_chai(tea,milk,suger):
    print(tea,milk,suger)

make_chai("latte","yup","low") #positioning

make_chai(tea="ginger",suger="high",milk="no") #keywords

def new_chai(*ingerdients,**extra):
    print("ingredients",ingerdients)
    print("extra",extra)

new_chai("ginger","sugar","milk",foam="yes",clove="no")