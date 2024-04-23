import os
"""Створіть абстрактний клас AbstractDevice з двома абстрактними методами: turn_on та turn_off.
Створіть клас-нащадок ConcreteDevice від абстрактного класу AbstractDevice,
який реалізовуватиме абстрактні методи батьківського класу."""

from abc import ABC, abstractmethod


class AbstractDevice(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class ConcreteDevice(AbstractDevice):

    def turn_on(self):
        print("Device is turned on")

    def turn_off(self):
        print("Device is turned off")


"""Створіть класи TV, Lights, Heating, кожен з яких має методи turn_on і turn_off для управління станом системи.
Створіть клас HomeFacade, який буде простим інтерфейсом для управління домом і буде інкапсулювати екземпляри класів
TV, Lights, Heating. Реалізуйте методи come_home і go_out у класі HomeFacade,
які будуть викликати методи включення та відключення у відповідних системах."""


class TV:

    def turn_on(self):
        return "TV was turned on"

    def turn_off(self):
        return "TV was turned off"


class Lights:
    def turn_on(self):
        return "Lights were turned on"

    def turn_off(self):
        return "Lights were turned off"


class Heating:
    def turn_on(self):
        return "Heating was turned on"

    def turn_off(self):
        return "Heating was turned off"


class HomeFacade:

    def __init__(self):
        self.__tv = TV()
        self.__lights = Lights()
        self.__heating = Heating()

    @property
    def tv(self):
        return self.__tv

    @property
    def lights(self):
        return self.__lights

    @property
    def heating(self):
        return self.__heating

    def come_home(self):
        self.tv.turn_on()
        self.lights.turn_on()
        self.heating.turn_on()

    def go_out(self):
        self.tv.turn_off()
        self.lights.turn_off()
        self.heating.turn_off()


"""3. Створіть власний клас контекстного менеджера MyContextManager, який дозволить управління ресурсом 
з використанням конструкції with. Реалізуйте методи __enter__ і __exit__ для власного контекстного менеджера.
 Наприклад, контекстний менеджер може відкривати файл у методі __enter__ і закривати його у методі __exit__."""


class MyContextManager:

    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(file=self.file_path, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Context manager executed with error')
        self.file.close()
        print("File was closed")


path = os.path.abspath("test_file.csv")


with MyContextManager(file_path=path, mode='r') as file:
    print(file.readlines())
