from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    def wait_until(self, locator, condition, timeout=10) -> WebElement:
        return wait(self.driver, timeout).until(condition(locator))

    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def element_is_visible(self, locator):
        self.go_to_element(self.element_is_present(locator))
        condition = ec.visibility_of_element_located
        return self.wait_until(locator, condition)

    def elements_are_visible(self, locator):
        condition = ec.visibility_of_all_elements_located
        return self.wait_until(locator, condition)

    def element_is_present(self, locator):
        condition = ec.presence_of_element_located
        return self.wait_until(locator, condition)

    def elements_are_present(self, locator):
        condition = ec.presence_of_all_elements_located
        return self.wait_until(locator, condition)

    def element_is_clickable(self, locator):
        condition = ec.visibility_of_element_located and ec.element_to_be_clickable
        return self.wait_until(locator, condition)

    def click(self, locator):
        self.go_to_element(self.element_is_present(locator))
        self.element_is_clickable(locator).click()

    def double_click(self, locator):
        element = self.element_is_visible(locator)
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, locator):
        element = self.element_is_visible(locator)
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def send_keys(self, locator, value):
        self.go_to_element(self.element_is_present(locator))
        condition = ec.visibility_of_element_located
        self.wait_until(locator, condition).send_keys(value)




