import time


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text
        #login page

    def wait_for_element_to_be_clickable(self, selector, selector_type=By.XPATH):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((selector_type, selector)))
        #login page

    def visibility_of_element_located(self, selector, selector_type=By.XPATH):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((selector_type, selector)))
        #remind_password_page


