"""1. Створити клас котрий буде мати class & instance attributes, getter & setter"""


class Laptop:

    def __init__(self, brand: str, gpu: int):
        self.__brand = brand
        self.__gpu = gpu

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def available_brands(self):
        """
        Method returns dict of available brands and number of items for each brand
        """
        brands = {'apple': 10, 'asus': 11, 'lenovo': 15, 'hp': 20, 'dell': 1, 'msi': 8}
        return brands

    def show_default_browser(self):
        return "Default browser is Edge"

    def check_items_left(self, brand):
        if self.brand in self.available_brands:
            return f"Number of {brand.capitalize()} laptops: {self.available_brands[brand]}"

    @classmethod
    def set_brand_items(cls, brand: str, number: int):
        if brand in cls.available_brands:
            cls.available_brands[brand] = number


"""2. Створити клас котрий буде успадковувати клас з першого завдання, та додати новий метод у CHILD клас"""


class Apple(Laptop):
    def __init__(self, brand, gpu, browser):
        self.browser = browser
        super().__init__(brand, gpu)

    def preorder(self):
        return "Pre-order successfully accepted"

    def show_default_browser(self):
        return f"Default browser is {self.browser}"


apple = Apple('apple', 2, 'Safari')
print(apple.preorder())
print(apple.show_default_browser())
