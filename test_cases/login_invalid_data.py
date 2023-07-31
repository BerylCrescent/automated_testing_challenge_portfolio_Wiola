import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginInvalidData(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system_invalid_data(self):
        user_login = LoginPage(self.driver)
       # user_login.title_of_page()
        user_login.type_in_email('user19@getnada.com')
        user_login.type_in_password('test-4321')
        user_login.click_on_the_sign_in_button()
        user_login.identifier_notification_located()
        dashboard_page = Dashboard(self.driver)
        user_login.screen_shot_plz('TC_01.png')
        dashboard_page.title_of_page()

    def test_log_in_to_the_system_invalid_email(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.type_in_email('users09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login.identifier_notification_located()
        dashboard_page = Dashboard(self.driver)
        user_login.screen_shot_plz('TC_03.png')
        dashboard_page.title_of_page()

    def test_log_in_to_the_system_invalid_password(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.type_in_email('user09@gatnada.com')
        user_login.type_in_password('test-4321')
        user_login.click_on_the_sign_in_button()
        user_login.identifier_notification_located()
        dashboard_page = Dashboard(self.driver)
        user_login.screen_shot_plz('TC_02.png')
        dashboard_page.title_of_page()

    def test_log_in_to_the_system_no_data(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.click_on_the_sign_in_button()
        user_login.please_provide_notification_located()
        dashboard_page = Dashboard(self.driver)
        user_login.screen_shot_plz('TC_04.png')
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
