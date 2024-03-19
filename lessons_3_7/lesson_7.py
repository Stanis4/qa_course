from typing import Callable, Union, Iterable

"""1. Напишіть самостійно функції котрі буде повторювати поведінку built-in функції map та filter"""


def my_map(func: Callable, iterable: Iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    print(result)


numbers = [1, 2, 3, 4]
my_map(lambda x: x ** 3, numbers)


def my_filter(func: Callable, iterable: Iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    print(result)


numbers = [1, 2, 3, 4, 5, 6]
my_filter(lambda x: x % 2 == 0, numbers)
my_map(lambda x: x % 2 == 0, numbers)


"""2. Напишіть функцію котра приймає 1 аргумент (int)(нехай це буде х) та повертає lambda функцію
 котра приймає один аргумент (нехай буде y) котрий буде піднесений до ступеня аргументу з функції (def),
  тобто змінна y буде піднесена до ступеня змінної х """


def take_to_pow(x: Union[int, float]):
    return lambda y: y ** x


square = take_to_pow(2.5)
result = round(square(5.66), 3)
# print(result)

"""3. Напишіть програму котра буде приймати назву функцій з консолі (input) (вони повинні існувати)
 та за допомогою built-in функції виводьте результат виконання переданої функції """


def print_hi():
    print("Hi")


def start_function():
    try:
        func = eval(input("Enter name of function: "))
    except NameError:
        print("Given function does not exist")
    else:
        if func is not None:
            func()

# start_function()
