"""1. Напишіть генератор котрий буде працювати як range() із агрументами start, stop & step"""


def custom_range_generator(start: int = 0, stop: int = 1, step: int = 1):
    if step == 0:
        raise ValueError("Zero step is not possible")
    value = start

    if start < stop and step > 0:
        while value < stop:
            yield value
            value += step
    elif start > stop and step < 0:
        while value > stop:
            yield value
            value += step
    else:
        raise ValueError("Unacceptable values are entered")


for item in custom_range_generator(10, 1, -1):
    print(item)


"""2. Напишіть generator comprehansion котрий буде повертати числа від 1 до 10"""

gen_comprehension = (item for item in custom_range_generator(1, 11))
for item in gen_comprehension:
    print(item)
