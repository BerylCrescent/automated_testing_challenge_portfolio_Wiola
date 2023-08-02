import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.remind_password_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPassword(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password_link_and_back_to_login_page(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.click_on_the_remind_password()
        remind_password_page = RemindPasswordPage(self.driver)
        #remind_password_page.title_of_page()
        remind_password_page.element_located()
        remind_password_page.screen_shot_plz('TC_08-1.png')
        remind_password_page.type_in_email('user09@getnada.com')
        remind_password_page.click_on_the_send_button()
        time.sleep(1)
        remind_password_page.screen_shot_plz('TC_08-3.png')
        remind_password_page.popup_located()
        remind_password_page.click_on_back_to_sign_in()
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        remind_password_page.screen_shot_plz('TC_08-2.png')

