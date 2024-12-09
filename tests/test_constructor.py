from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestsConstructor:
    def test_toppings_click_see_toppings(self, driver):  # Проверка перехода на топпинги
        driver.find_element(*Locators.TOPPINGS).click()
        assert EC.visibility_of_element_located(Locators.TEG_TOPPINGS)


    def test_buns_click_across_toppings_see_buns(self, driver):  # Проверка перехода на булки
        TestsConstructor.test_toppings_click_see_toppings(self, driver)
        driver.find_element(*Locators.BUNS).click()
        assert EC.visibility_of_element_located(Locators.TEG_BUNS)


    def test_sauces_click_across_toppings_see_sauces(self, driver):  # Проверка перехода на соусы
        TestsConstructor.test_toppings_click_see_toppings(self, driver)
        driver.find_element(*Locators.SOUSES).click()
        assert EC.visibility_of_element_located(Locators.TEG_SOUSES)
