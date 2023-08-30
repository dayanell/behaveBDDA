from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=5) -> WebElement:
        self.wait_until_element_is_visible(locator, timeout)
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def wait_until_element_is_visible(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def current_url(self):
        return self.driver.current_url
