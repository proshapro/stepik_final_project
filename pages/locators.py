from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".add-to-basket button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    PRODUCT_NAME_IN_SUCCESS_ALERT = (By.XPATH, "//text()[contains(.,'has been added')]//preceding-sibling::strong")
    PRICE_IN_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
