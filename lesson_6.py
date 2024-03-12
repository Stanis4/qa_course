import math

"""1. Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
 Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями."""


def sum_range(start: int, end: int) -> int:
    try:
        if start < end:
            count_sum = sum(range(start, end + 1))
        else:
            count_sum = sum(range(end, start + 1))
    except TypeError:
        print("Only integer type is allowed")
    else:
        return count_sum


# print(sum_range(2, 5))
# print(sum_range(5, 2))

"""2. Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
 периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх"""


def square(quadrant_side):
    quadrant_perimeter = quadrant_side * 4
    quadrant_square = quadrant_side ** 2
    quadrant_diagonal = quadrant_side * math.sqrt(2)

    print("Side:", quadrant_side)
    print("Perimeter:", quadrant_perimeter)
    print("Square:", quadrant_square)
    print("Diagonal:", quadrant_diagonal)


# square(5)

"""3. Напишіть 2 функції котрі:
1. Приймає ввід від юзера з консолі та повертає введене значення, приклад вводу
2. Приймає результат виконання першої функції та друкує повідомлення у консоль
"User is going to work with (there is data type)" """


def user_input():
    value = input("Enter your value: ")
    return value


def define_input_type(user_value):
    try:
        input_type = (type(eval(user_value)))
    except NameError:
        print("Unknown data type")
    else:
        print(f"User is going to work with {input_type.__name__}")


define_input_type(user_input())
