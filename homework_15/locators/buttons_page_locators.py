from selenium.webdriver.common.by import By


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    # result messages
    DOUBLE_CLICK_BUTTON_MESSAGE = (By.XPATH, "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_BUTTON_MESSAGE = (By.XPATH, "//p[@id='rightClickMessage']")
    CLICK_BUTTON_MESSAGE = (By.XPATH, "//p[@id='dynamicClickMessage']")
