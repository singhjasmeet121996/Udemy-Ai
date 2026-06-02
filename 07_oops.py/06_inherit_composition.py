class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def Prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding more masala")


class Chaishop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai=self.chai_cls("Reg")

    def serve(self):
        print(f"Serving {self.chai.type} Chai")
        self.chai.Prepare()

class FancyChaiShop(Chaishop):
    chai_cls = MasalaChai


shop = Chaishop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()