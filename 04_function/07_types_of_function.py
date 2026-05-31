def pure_chai(cups):
    return cups * 10

total_chai = 0

def impure_chai():
    global total_chai
    total_chai =+ total_chai

def pour_chai(n):
    print(n)
    if n == 0:
        return "done"
    return pour_chai(n-1) 

print(pour_chai(4))