"""1. Створити клас котрий буде мати class & instance attributes, getter & setter"""


class Laptop:
    # brands and number of items
    brands = {'apple': 10, 'asus': 11, 'lenovo': 15, 'hp': 20, 'dell': 1, 'msi': 8}

    def __init__(self, brand: str, gpu: int):
        self.brand = brand
        self.gpu = gpu

    def get_entered_values(self):
        return f"Brand: {self.brand}, gpu: {self.gpu}"

    def show_default_browser(self):
        return "Default browser is Edge"

    def check_items_left(self, brand):
        if self.brand in self.brands:
            return f"Number of {brand.capitalize()} laptops: {self.brands[brand]}"

    def set_gpu(self, new_gpu):
        self.gpu = new_gpu

    @classmethod
    def set_brand_items(cls, brand: str, number: int):
        if brand in cls.brands:
            cls.brands[brand] = number


laptop = Laptop('hp', 16)
print(laptop.get_entered_values())

laptop.set_gpu(24)
print(laptop.get_entered_values())

print(laptop.check_items_left('apple'))
laptop.set_brand_items('apple', 9)
print(laptop.check_items_left('apple'))

"""2. Створити клас котрий буде успадковувати клас з першого завдання, та додати новий метод у CHILD клас"""


class Apple(Laptop):
    def __init__(self, brand, gpu, browser):
        super().__init__(brand, gpu)
        self.browser = browser

    def preorder(self):
        return "Pre-order successfully accepted"

    def show_default_browser(self):
        return f"Default browser is {self.browser}"


apple = Apple('apple', 2, 'Safari')
print(apple.preorder())
print(apple.show_default_browser())
