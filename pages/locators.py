from selenium.webdriver.common.by import By

class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, '')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href$="/basket/"]')

class LoginPageLocators():
    REGISTER_FORM = (By.CLASS_NAME, 'register_form')
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    CHECK_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')

