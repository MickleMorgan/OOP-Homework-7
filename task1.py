def doubler(item):
    return item * 2


def custom_sequence(start, num_elements, user_func):
    count = 0
    while count < num_elements:
        yield user_func(start)
        start += 1
        count += 1


for i in custom_sequence(1, 30, doubler):
    print(i)