def four(num):
    x = 0
    while x < num:
        print("in generator, x =", x)
        yield x
        x += 1


# generate any number of numbers
for i in four(5):
    print(i)


def four(start, num):
    x = start
    while x < num:
        print("in generator, x =", x)
        yield x
        x += 1


# generate any number of numbers with an initial value
for i in four(2, 5):
    print(i)
