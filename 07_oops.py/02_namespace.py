class Chai:
    origin = "india"

print(Chai.origin)

Chai.is_hot=True

print(Chai.is_hot)

#Creating objs from class

masala = Chai()
print(masala.origin,"form masala")
print(masala.is_hot,"form masala")

masala.is_hot = False
print(masala.is_hot,"form masala")