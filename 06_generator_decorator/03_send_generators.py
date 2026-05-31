def chai_cust():
    print("welcome: what kind of chai you like?")
    order = yield
    while True:
        print(f"prep: {order}")
        order = yield

stall =chai_cust()
next(stall)

stall.send("masala")
stall.send("garam")