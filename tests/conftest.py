import pytest
from selenium import webdriver
from tests.constants import Constants
from tests.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.HOME_PAGE)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.PER_OFFISE).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.INPUT))
    driver.find_element(*Locators.LOGIN).send_keys(*Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(*Constants.PASSWORD)
    driver.find_element(*Locators.INPUT).click()
    return driver







