import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.add_player_page import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        time.sleep(3)
        dashboard_page.click_add_player_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_page()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()
