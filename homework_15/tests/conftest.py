import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from homework_15.driver.driver_factory import driver_factory



@pytest.fixture(scope='function')
def driver(request):
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = driver_factory('chrome')
    driver.maximize_window()
    url = request.node.get_closest_marker('url')
    driver.get(url.args[0])
    yield driver
    driver.quit()
