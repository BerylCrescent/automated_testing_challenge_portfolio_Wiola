import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.remind_password_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestHyperlinkLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_hyperlink_login_page_response(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_the_remind_password()
        remind_password_page = RemindPasswordPage(self.driver)
        user_login.screen_shot_plz('TC_06-1.png')
        remind_password_page.title_of_page()
        remind_password_page.click_on_back_to_sign_in()
        user_login = LoginPage(self.driver)
        user_login.screen_shot_plz('TC_06-2.png')
        user_login.title_of_page()
