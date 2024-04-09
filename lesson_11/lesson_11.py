"""1. Створити клас котрий буде мати class & instance attributes, getter & setter"""


class Laptop:
    shop = 'Amazon'

    def __init__(self, brand: str, gpu: int):
        self.__brand = brand
        self.__gpu = gpu

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    def show_default_browser(self):
        return "Default browser is Edge"


"""2. Створити клас котрий буде успадковувати клас з першого завдання, та додати новий метод у CHILD клас"""


class Apple(Laptop):
    def __init__(self, brand: str, gpu: int, browser: str):
        self.browser = browser
        super().__init__(brand, gpu)

    def preorder(self):
        return "Pre-order successfully accepted"

    def show_default_browser(self):
        return f"Default browser is {self.browser}"


apple = Apple('apple', 2, 'Safari')
print(apple.preorder())
print(apple.show_default_browser())
