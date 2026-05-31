def local_chai():
    yield "masala"
    yield "kadak"
    yield "garam"

def import_chai():
    yield "latte"
    yield "coco"

def ful_menu():
    yield from local_chai()
    yield from import_chai()

for chai in ful_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield"waiting for order"
    except:
        print("closing time")

stall = chai_stall()
print(next(stall))

stall.close()