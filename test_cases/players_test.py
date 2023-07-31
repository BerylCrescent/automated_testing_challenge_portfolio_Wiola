import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestPlayersSearch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_search_filter_table(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_players()
        players_page = PlayersPage(self.driver)
        players_page.fill_filter_table('Michael', 'Kelso', 'Kettlehead', 'Point Place')
        players_page.choose_columns()
        players_page.screen_shot_plz('TC_09.png')


    @classmethod
    def tearDown(self):
        self.driver.quit()
