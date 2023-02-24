def doubler(item):
    return item * 2


def function_for_list(sequence, func):
    return sum(func(item) for item in sequence)


n = [0, 1, 2, 3]
print(function_for_list(n, doubler))
