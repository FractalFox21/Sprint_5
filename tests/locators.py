from selenium.webdriver.common.by import By

class Locators:

    PER_OFFISE = (By.XPATH, ".//p[text()='Личный Кабинет']") #кнопка личного кабинета
    REG_BUTTON = (By.XPATH, './/a[text()="Зарегистрироваться"]')    #кнопка перехода к странице регистрации
    REG_NAME = (By.XPATH, ".//fieldset[1]/div/div/input")   #Поле ввода имени при регистрации
    REG_EMAIL = (By.XPATH, ".//fieldset[2]/div/div/input" )  #Поле ввода Email при регистрации
    REG_PASSWORD = (By.XPATH, ".//fieldset[3]/div/div/input" )  #Поле ввода пароля при регистрации
    FIN_REG = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]") #Кнопка отправки заявки на регистрацию
    LOGO = (By.XPATH, ".//nav/div/a")  #логотип сайта
    CONSTR = (By.XPATH, ".// p[contains(text(), 'Конструктор')]")

    #авторизация
    LOGIN = (By.XPATH, ".//fieldset[1]/div/div/input")  #Поле ввода email
    PASSWORD = (By.XPATH, ".//fieldset[2]/div/div/input")   #Поле ввода пароля
    INPUT = (By.XPATH, "//button[contains(text(),'Войти')]")     #Кнопка входа
    ORDER = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]") #Кнопка "оформить заказ" для проверки авторизации
    LOGOUT = (By.XPATH, ".//button[contains(text(),'Выход')]")
