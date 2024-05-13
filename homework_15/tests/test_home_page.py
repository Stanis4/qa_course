import pytest
from homework_15.locators.home_page_locators import HomePageLocators
from homework_15.pages.home_page import HomePage
from homework_15 import config


@pytest.mark.url(config.browser.base_url)
class TestHomePage:
    def test_list_of_cards(self, driver):
        home_page = HomePage(driver)
        expected_number_of_cards = 6
        actual_number_of_cards = home_page.count_number_of_cards()
        assert expected_number_of_cards == actual_number_of_cards, (f'Number of cards is {actual_number_of_cards}, '
                                                                    f'expected number is {expected_number_of_cards}')

    def test_cards_are_clickable(self, driver):
        home_page = HomePage(driver)
        card_list = home_page.elements_are_visible(HomePageLocators.CATEGORY_CARDS_LIST)
        for card in card_list:
            assert home_page.element_is_clickable(card), f'Element {card} is not clickable'
