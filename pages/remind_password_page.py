#import time

from pages.base_page import BasePage

from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RemindPasswordPage(BasePage):
    back_to_sign_in_hyperlink_xpath = "//a[text()='Back to sign in']"
    change_language_english_xpath = "//div[@role='button']"
    email_field_xpath = "//input[@name='email']"
    remind_password_head_xpath = "//h5[text()='Remind password']"
    remind_password_url = "https://scouts-test.futbolkolektyw.pl/en/remind"
    send_button_xpath = "//button[@type='submit']"
    expected_title = 'Remind password'


    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def click_on_the_send_button(self):
        self.click_on_the_element(self.send_button_xpath)

    def click_on_back_to_sign_in(self):
        self.click_on_the_element(self.back_to_sign_in_hyperlink_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.remind_password_url) == self.expected_title

    def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)

    def element_located(self):
        self.visibility_of_element_located(self.send_button_xpath)

