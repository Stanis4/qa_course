import pytest
import homework_15.config as config
from homework_15.driver.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(request):
    url = config.browser.base_url

    if request.node.get_closest_marker('route'):
        url += request.node.get_closest_marker('route').args[0]

    driver = driver_factory('chrome')
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
