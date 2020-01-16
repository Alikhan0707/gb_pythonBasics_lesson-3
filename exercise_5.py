def sumOfList(y):

    int_list = []

    for i in y:

        int_list.append(int(i))

    return sum(int_list)


c = 0

while True:

    a = input("Enter numbers separated by spaces: ")

    y = a.split(' ')

    if 'q' in y:

        y.remove('q')

        current_sum = sumOfList(y)
        c += sumOfList(y)

        print(current_sum)
        print(c)

        break

    else:

        current_sum = sumOfList(y)
        c += sumOfList(y)

        print(current_sum)
        print(c)
