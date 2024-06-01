from selenium.webdriver.remote.webdriver import WebDriver
from homework_15.pages.base_page import BasePage
from homework_15.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    locators = HomePageLocators()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def count_number_of_cards(self):
        return len(self.elements_are_visible(self.locators.CATEGORY_CARDS_LIST))


