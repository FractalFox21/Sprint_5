from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestsLogin:

    def test_button_log_in_home_page_login_home_page(self, driver):    #вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.HOME_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT))
        driver.find_element(*Locators.LOGIN).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.INPUT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.HOME_PAGE))
        current_url = driver.current_url
        assert Constants.HOME_PAGE == current_url

    def test_button_per_office_login_home_page(self, driver): #вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.PER_OFFICE).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT))
        driver.find_element(*Locators.LOGIN).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.INPUT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.HOME_PAGE))
        current_url = driver.current_url
        assert Constants.HOME_PAGE == current_url

    def test_login_across_reg_login_home_page(self,driver):     #вход через кнопку "вход" в форме регистрации
        driver.find_element(*Locators.PER_OFFICE).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIN_REG))
        driver.find_element(*Locators.ALREADY_REG_INPUT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT))
        driver.find_element(*Locators.LOGIN).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.INPUT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.HOME_PAGE))
        current_url = driver.current_url
        assert Constants.HOME_PAGE == current_url

    def test_login_across_reset_password_login_home_page(self,driver):       #вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.PER_OFFICE).click()
        driver.find_element(*Locators.RESET_PASS).click()
        driver.find_element(*Locators.REMEMBERED_INPUT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT))
        driver.find_element(*Locators.LOGIN).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.INPUT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.HOME_PAGE))
        current_url = driver.current_url
        assert Constants.HOME_PAGE == current_url

