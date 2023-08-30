from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserHomePage(BasePage):
    __url = "https://vue-vuex-realworld.netlify.app/#/"
    __username = (By.CSS_SELECTOR, "li:nth-of-type(4) > .nav-link")

    def __init__(self, driver):
        super().__init__(driver)

    def user_identification(self, ):
        user_text = self.get_text(self.__username)
        return user_text.strip()
