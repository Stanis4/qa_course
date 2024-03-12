import math

"""1. Написати програму, яка запитує у користувача число і обчислює його квадратний корінь."""
"""2. Модифікувати попередню програму так, щоб вона також обробляла помилку введення,
 коли введене значення не може бути перетворене на число (ValueError),"""


class NegativeNumberIsNotAcceptableException(Exception):
    pass


class IncorrectFractionalNumberException(Exception):
    pass


class UnexpectedErrorException(Exception):
    pass


def find_square_root():
    print("Find Square root of number. Acceptable format: 7 --- 7.0 --- 2/5 --- 2 2/5")
    try:
        number = input("Enter your number: ")
        if number.endswith("/"):
            raise IncorrectFractionalNumberException("Please recheck the fractional number. It's incomplete")
        refined_number = _refine_number(number)
        if refined_number < 0:
            raise NegativeNumberIsNotAcceptableException("Negative number is not acceptable for this operation")
        else:
            result = math.sqrt(refined_number)
            print(f"Square root of {number}:", result)
    except ValueError as error:
        print("Only numbers are allowed:", error.__repr__())
    except UnexpectedErrorException as error:
        print("Unexpected error appeared. Try again.", error)
    finally:
        print("Calculation is finished")


def _refine_number(number):
    try:
        if not isinstance(number, int) and not isinstance(number, float):
            result = refined_input = number.replace("/", " ").replace("\\", " ").replace(",", ".").strip().split()
            if len(refined_input) == 3:
                multiplier = float(refined_input[0])
                numerator = float(refined_input[1])
                denominator = float(refined_input[2])
                result = [((denominator * multiplier) + numerator) / denominator]
            elif len(refined_input) == 2:
                result = [float(refined_input[0]) / float(refined_input[1])]
        else:
            result = float(number)
    except ZeroDivisionError:
        print("Denominator cannot be 0")
    except Exception as error:
        print("Unexpected error appeared", error.__repr__())
    else:
        return float(result[0])


"""3. Розширити роботу нашого калькулятора, додавши можливість користувачеві вводити числа до тих пір,
 поки він не вирішить вийти, вводячи певне ключове слово (наприклад, "вихід")."""


def calculator():
    exit_word = "q"
    while True:
        try:
            number1 = input("Number 1 (enter 'q' to quit): ").replace(",", ".")
            if number1 == exit_word:
                break
            else:
                number1 = float(number1)

            number2 = input("Number 2 (enter 'q' to quit): ").replace(",", ".")
            if number2 == exit_word:
                break
            else:
                number2 = float(number2)

            action = input("Action (enter 'q' to quit): ")
            if action == exit_word:
                break

            if action not in ("+", "-", "*", "/"):
                raise ValueError("The entered action is not possible: ", action)

            if action == "+":
                print(number1 + number2)
            elif action == "-":
                print(number1 - number2)
            elif action == "*":
                print(number1 * number2)
            elif action == "/":
                if number2 == 0:
                    raise ZeroDivisionError("Division by 0 is not possible")
                print(number1 / number2)
        except ValueError as e:
            print("Error:", e)
            print("Please recheck entered values.")
        except ZeroDivisionError as e:
            print("Error:", e)
        except Exception as e:
            print("Error appeared ->", e)
            print("Please recheck entered values. Enter 'q' to quit")

    print("Calculator is closed")


find_square_root()
# calculator()
