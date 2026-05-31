def infine_chai():
    count = 1
    while True:
        yield f"refil {count}"
        count += 1

refill= infine_chai()

for _ in range(3):
    print(next(refill))