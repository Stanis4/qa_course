from selenium.webdriver.remote.webdriver import WebDriver
from homework_15.pages.base_page import BasePage
from homework_15.locators.buttons_page_locators import ButtonsPageLocators


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_action(self):
        self.click(self.locators.CLICK_BUTTON)
        return self.check_click_result(self.locators.CLICK_BUTTON_MESSAGE)

    def double_click_action(self):
        dc_b = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.double_click(self.locators.DOUBLE_CLICK_BUTTON)
        return self.check_click_result(self.locators.DOUBLE_CLICK_BUTTON_MESSAGE)

    def right_click_action(self):
        self.right_click(self.locators.RIGHT_CLICK_BUTTON)
        return self.check_click_result(self.locators.RIGHT_CLICK_BUTTON_MESSAGE)

    def check_click_result(self, locator):
        return self.element_is_present(locator).text
