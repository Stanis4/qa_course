import time

"""1. Створіть декоратор, який повертає результат функції, а також час за який вона виконана"""


def time_log(func):
    def inner():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time of func execution of {func.__name__} function: ", execution_time)
        return result
    return inner


@time_log
def range_generator():
    return [i for i in range(10000) if i % 2 == 0]


print(range_generator())

"""2. Створіть декоратор, котрий приймає аргумент, аргумент повинен бути рядком та
 роздрукований за допомогою print перед виконанням функції (тобто зробимо примітивний логер)"""


def logger(message: str):
    def print_log(func):
        def wrap(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result
        return wrap
    return print_log


@logger('This function will sum of 2 ints')
def plus(x, y):
    return x + y


print(plus(10, 20))
