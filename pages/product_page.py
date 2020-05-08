from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_success_message(self):
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert self.product_name() == product_name_in_alert, f"Expected {self.product_name()} in success message, " \
                                                             f"received {product_name_in_alert} instead "

    def should_be_correct_product_price_in_info_message(self):
        product_price_in_alert = self.browser.find_element(*ProductPageLocators.PRICE_IN_INFO_MESSAGE).text
        assert self.product_price() == product_price_in_alert, f"Price from info message({product_price_in_alert}) " \
                                                               f"does not match the price of the product added to the" \
                                                               f" basket({self.product_price()}) "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
