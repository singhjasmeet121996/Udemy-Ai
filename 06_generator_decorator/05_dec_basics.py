def my_dec(func):
    def wrapper():
        print("before running")
        func()
        print("after running")
    return wrapper

@my_dec
def greet():
    print("yo")

greet()