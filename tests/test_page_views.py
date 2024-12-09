from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestsPageWiews:

    def test_profile_login_click_open_profile(self, driver, login):     #Проверка открытия страницы профиля
        driver.find_element(*Locators.PER_OFFICE).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOUT))
        current_url = driver.current_url
        assert Constants.PROFILE_URL == current_url

    def test_constructor_across_profile_profile_open_constructor(self, driver, login):      #Проверка перехода на страницу конструктора (главная) из профиля
        TestsPageWiews.test_profile_login_click_open_profile(self, driver, login)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT))
        driver.find_element(*Locators.CONSTR).click()
        current_url = driver.current_url
        assert current_url == Constants.HOME_PAGE

    def test_logo_across_profile_profile_open_home(self, driver, login):    #Проверка перехода на главную страницу по логотипу сайта из профиля
        TestsPageWiews.test_profile_login_click_open_profile(self, driver, login)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO))
        driver.find_element(*Locators.LOGO).click()
        current_url = driver.current_url
        assert current_url == Constants.HOME_PAGE


    def test_logout_profile_page_login(self,driver, login):     #Проверка выхода из профиля
        TestsPageWiews.test_profile_login_click_open_profile(self, driver, login)
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT))
        current_url = driver.current_url
        assert current_url == Constants.LOGIN_PAGE


