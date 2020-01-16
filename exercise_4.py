# First method of raising x to the power of y


def pow_first_meth(x, y):

    c = x ** (-y)

    return 1 / c

# Second method of raising x to the power of y by using of cicle


def pow_second_meth(x, y):

    d = y * -1

    i = 0

    c = 1

    while i < d:

        c *= x

        i += 1

    return 1 / c

x = float(input("Enter a real positive number: "))
y = int(input("Enter a negative integer: "))

print(pow_first_meth(x, y))
print(pow_second_meth(x, y))

