import timeit

stmt_1 = '''
def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_sequence(n-1) + fibonacci_sequence(n-2))
fibonacci_sequence(30)
'''
stmt_2 = '''
import functools

@functools.lru_cache
def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_sequence(n-1) + fibonacci_sequence(n-2))
fibonacci_sequence(30)
'''

stmt_3 = '''
def fibonacci_sequence_memo():
    buffer = [1, 1]

    def next_member(number):
        if number < len(buffer):
            return buffer[number]

        current, next = buffer[-2], buffer[-1]
        counter = len(buffer)
        while counter <= number:
            current, next = next, current + next
            buffer.append(next)
            counter += 1
        return next

    return next_member
f = fibonacci_sequence_memo()
f(30)
'''
print(timeit.timeit(stmt_1, number=10))
print(timeit.timeit(stmt_2, number=10))
print(timeit.timeit(stmt_3, number=10))