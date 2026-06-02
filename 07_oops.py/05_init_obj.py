class ChaiOrder:
    def __init__(self, type_, size):  
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} Chai"

order = ChaiOrder("malasa",200)
print(order.summary())
order_2 = ChaiOrder("ginger",230)
print(order.summary())