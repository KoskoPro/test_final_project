from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.should_be_add_basket_form()
        self.adding_product_to_basket()

    def should_be_add_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket form is not presented"

    def adding_product_to_basket(self):
        add_to = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to.click()

    def check_product_name(self):
        text_add_product = self.browser.find_element(*ProductPageLocators.CHECK_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert text_add_product == product_name, "Wrong basket product name"

    def check_product_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, "Wrong basket product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CHECK_BASKET),\
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.CHECK_BASKET),\
            "Success message is not presented, but should be"