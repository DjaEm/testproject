from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTRATION = (By.ID, "id_registration-email")
    PASSWORD_REGISTRATION = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CHECK_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
