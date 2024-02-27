x_var = 0
y_var = 0
print("out layer-> x_var: {0} y_var: {1}".format(x_var, y_var))


def test1():
    y_var = 2
    print("in test1-> x_var: {0} y_var: {1}".format(x_var, y_var))

    def test2():
        global x_var
        nonlocal y_var

        x_var = 1
        y_var = 4

        print("in test2-> x_var: {0} y_var: {1}".format(x_var, y_var))

    test2()
    print("in test1-> x_var: {0} y_var: {1}".format(x_var, y_var))


test1()
print("out layer-> x_var: {0} y_var: {1}".format(x_var, y_var))