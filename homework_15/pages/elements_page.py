from selenium.webdriver.remote.webdriver import WebDriver
from homework_15.generator.generator import generated_person
from homework_15.pages.base_page import BasePage
from homework_15.locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.send_keys(self.locators.FULL_NAME, full_name)
        self.send_keys(self.locators.EMAIL, email)
        self.send_keys(self.locators.CURRENT_ADDRESS, current_address)
        self.send_keys(self.locators.PERMANENT_ADDRESS, permanent_address)
        self.click(self.locators.SUBMIT)
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
