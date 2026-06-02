class Chai_cup:
    size = 150
    def desc(self):
        return f"a {self.size} ml"


cup = Chai_cup()
print(cup.desc())