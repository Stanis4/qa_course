import pytest
from homework_15.pages.buttons_page import ButtonsPage


@pytest.mark.route('buttons')
class TestButtons:
    def test_buttons(self, driver):
        buttons_page = ButtonsPage(driver)

        double_click = buttons_page.double_click_action()
        right_click = buttons_page.right_click_action()
        click = buttons_page.click_action()

        assert double_click == "You have done a double click", "Double click action failed"
        assert right_click == "You have done a right click", "Right click action failed"
        assert click == "You have done a dynamic click", "Dynamic click action failed"
