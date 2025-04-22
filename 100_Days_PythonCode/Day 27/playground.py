def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6,2,1,5))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")     #we use get if the key does not exist in the dictionary, it will not return an
                                            # error in the console and it will run without problems
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

