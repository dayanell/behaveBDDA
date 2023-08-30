from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SignInPage(BasePage):
    __url = "https://vue-vuex-realworld.netlify.app/#/login"
    __email_field = (By.CSS_SELECTOR, 'input[placeholder="Email"]')
    __password_field = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
    __sign_in_button = (By.XPATH, "//button[normalize-space()='Sign in']")
    __page_header = (By.TAG_NAME, "h1")
    __error_message = (By.CSS_SELECTOR, "div[class='auth-page'] li:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self):
        self.driver.get(self.__url)

    @property
    def expected_url(self):
        return self.__url

    @property
    def page_header(self):
        return self.get_text(self.__page_header)

    def type_email(self, email):
        email_input = self.find(self.__email_field)
        if email == "None":
            email_input.clear()
        else:
            self.type(self.__email_field, email)

    def type_password(self, password):
        password_input = self.find(self.__password_field)
        if password == "None":
            password_input.clear()
        else:
            self.type(self.__password_field, password)

    def click_submit_button(self):
        self.click(self.__sign_in_button)

    def error_message_is_displayed(self) -> bool:
        return self.is_displayed(self.__error_message)

    def error_message_description(self) -> str:
        return self.get_text(self.__error_message)
