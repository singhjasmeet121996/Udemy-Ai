def serve_chai():
    yield "masala cup"
    yield "ginger cup"
    yield "elachi cup"

stall = serve_chai()

for cup in stall:
    print(cup)