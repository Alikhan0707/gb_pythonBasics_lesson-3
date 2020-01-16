def my_func(a, b, c):
    new_list = [a, b, c]

    min_num = min(new_list)

    new_list.remove(min_num)

    return sum(new_list)

print(my_func(5, 2, 3))