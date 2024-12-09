from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

faker = Faker()

class TestNewUsers:
    def test_reg_new_user_well_reg(self,driver):
        email = faker.email()
        driver.find_element(*Locators.PER_OFFICE).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIN_REG))
        driver.find_element(*Locators.REG_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(Constants.REG_PASS)
        driver.find_element(*Locators.FIN_REG).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.LOGIN_PAGE))
        current_url = driver.current_url
        assert current_url == Constants.LOGIN_PAGE

    def test_reg_short_pass_stay_on_page(self,driver):
        email = faker.email()
        driver.find_element(*Locators.PER_OFFICE).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIN_REG))
        driver.find_element(*Locators.REG_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(Constants.REG_SHORT_PASS)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIN_REG))
        driver.find_element(*Locators.FIN_REG).click()
        assert EC.visibility_of_element_located(Locators.REG_ERROR)
