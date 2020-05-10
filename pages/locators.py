from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".register_form button")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".add-to-basket button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.XPATH, "//text()[contains(.,'has been added')]//preceding-sibling::strong")
    PRICE_IN_INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//text()[contains(.,'basket is empty')]//parent::p")
