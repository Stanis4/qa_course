"""1 - Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
 перетворити рядок, щоб кожне ім'я явно починалися з великої літери."""


def capitalize_names():
    names_list = ["john", "marta", "james", "amanda", "marianna"]
    new_list = []
    for name in names_list:
        new_list.append(name.capitalize())
    print(new_list)


"""2 - У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"]
 перетворити його у список змінних для Пайтона snake_case, "friends_list", "my_tuple"]"""


def transform_to_snake_case():
    words = ["FirstItem", "FriendsList", "MyTuple"]
    new_list = []
    for word in words:
        new_word = ""
        for letter in word:
            if letter.isupper():
                new_word += "_" + letter.lower()
            else:
                new_word += letter.lower()
        new_list.append(new_word.lstrip("_"))

    print(new_list)


""" 3. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
 Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python. 
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
Виведіть словник на екран."""


def programming_languages():
    languages = {"Python": "Guido van Rossum",
                 "Java": "James Gosling",
                 "C++": "Bjarne Stroustrup",
                 "JavaScript": "Brendan Eich"}
    for language, founder in languages.items():
        print(f"My favorite programming language is {language}. It was created by {founder}.")

    remove_element = "C++"
    print(f"Remove element {remove_element}")

    languages.pop(remove_element)
    print("Updated dictionary: \n", languages)


"""4- Дан лист: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
Використовуючи continue виведіть тілько імена у консоль"""


def get_names():
    names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
    # solution 1
    print([name for name in names if isinstance(name, str)])
    # solution 2
    for name in names:
        if not isinstance(name, str):
            continue
        print(name)


"""5. Дан лист types=[1, 1000, 2, 12, {'key': 'value'}
Використовуючи break напишіть програму котра буде виводити тільки int тип даних, 
якщо тип буде інший зупинити цикл з повідомленням 
f'цикл не працює з {тут тип даних із-за якого ми зупинили цикл} типом даних'"""


def get_int_values():
    types = [1, 1000, 2, 12, {'key': 'value'}]
    for item in types:
        if type(item) is not int:
            print(f"цикл не працює з {type(item)} типом даних")
            break
        else:
            print(item)


"""6 - Напишіть програму котра підраховує кількість однакових символів у значенні котре введе користувач в консолі"""


def count_similar_elements():
    text = input("Enter your text here: ")
    elements_counter = {}
    for letter in text:
        elements_counter[letter] = text.count(letter)

    result = ",".join([f"{letter},{count}" for letter, count in elements_counter.items()])
    print(result)


"""7. Перепишіть калькулятор, який буде продовжувати працювати при невірно введених даних юзером
Додаткова умова: у юзера буде всього 2 спросили ввести правильні значення, 
після другої спроби програма повинна завершуватись з повідомленням Спроси скінчились"""


def calculator():
    counter = 2
    while counter != 0:
        try:
            number1 = float(input("Number 1: ").replace(",", "."))
            number2 = float(input("Number 2: ").replace(",", "."))
            action = input("Action: ")

            if action not in ("+", "-", "*", "/"):
                raise ValueError("The entered action is not possible: ", action)
            if action == "+":
                print((number1 + number2))
            elif action == "-":
                print((number1 - number2))
            elif action == "*":
                print((number1 * number2))
            elif action == "/":
                print((number1 / number2))
        except Exception as e:
            counter -= 1
            print("Error appeared ->", e)
            print("Please recheck entered values. Only numbers are allowed.")
            if counter == 0:
                print("You have no more attempts")
                break
            continue
        break


if __name__ == "__main__":
    capitalize_names()
    # transform_to_snake_case()
    # programming_languages()
    # get_names()
    # get_int_values()
    # count_similar_elements()
    # calculator()
