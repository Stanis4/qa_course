"""Task 1. Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'"""


# solution 1 (using string methods)
def is_palindrome():
    word = input("Enter your word here: ").lower()
    if word != "":
        reversed_string = "".join(reversed(word))
        if reversed_string == word:
            print("+")
        else:
            print("-")
    else:
        print("Something went wrong. Try again")


# solution 2 (using list slicing)
def is_palindrome_2():
    word = input("Enter your word here: ").lower()
    if word:
        if word == word[::-1]:
            print("+")
        else:
            print("-")
    else:
        print("Something went wrong. Try again")


"""Task 2.Користувач вводить текст і слово, яке потрібно знайти, 
          якщо це слово є в тексті, вивести 'YES', інакше 'NO'"""


def is_in_text():
    text = input("Enter text here: ")
    search_word = input("Enter word to search: ")

    if text and search_word:
        if search_word in text:
            print('YES')
        else:
            print('NO')
    else:
        print("Check your input data")


"""Task 3.Написати валідатор для пошти. Користувач вводить пошту,
   а програма повинна перевірити, що в пошті є символ '@' і '.', 
   і якщо це так, вивести "YES", інакше "NO"""


def email_validator():
    email = input("Enter your email here: ")
    if email:
        if '@' in email and '.' in email:
            print("YES")
        else:
            print("NO")
    else:
        print("Email is not entered")


"""Task 4.Користувач вводить текст через пробіл. Конвертувати текст у список. 
          Вивести останні 3 елементи зі списку, якщо список містить менше 3-х елементів, 
          вивести повідомлення про те що кількість елементів менша за 3 
          і вказати кількість елементів поточного списку"""


def convert_to_list():
    text = input("Enter your text here: ")
    if text:
        text_list = text.strip().split(" ")

        if len(text_list) >= 3:
            print(text_list[-3:])
        else:
            print("Number of elements is", len(text_list), "which is less than 3")
    else:
        print("The text is missing")


if __name__ == "__main__":
    is_palindrome()
    is_palindrome_2()
    is_in_text()
    email_validator()
    convert_to_list()
