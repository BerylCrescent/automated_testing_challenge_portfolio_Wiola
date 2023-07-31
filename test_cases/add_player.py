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
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        #dashboard_page.title_of_page()
        dashboard_page.click_add_player_button()
        add_player_page = AddPlayer(self.driver)
        #add_player_page.title_of_page()
        add_player_page.type_in_email('kettlehead@vp.pl')
        add_player_page.type_in_name('Michael')
        add_player_page.type_in_surname('Kelso')
        add_player_page.type_in_phone('500555005')
        add_player_page.type_in_weight('55')
        add_player_page.type_in_height('182')
        add_player_page.type_in_club('Point Place')
        add_player_page.type_in_second_position('Officer')
        add_player_page.click_leg_select()
        add_player_page.click_district_select()
        add_player_page.type_in_main_position('Kettlehead')
        add_player_page.type_in_age('11.11.2011')
        add_player_page.type_in_level('None')
        add_player_page.type_in_achievements('None')
        add_player_page.type_in_language('Polish')
        add_player_page.type_in_laczy('Tak')
        add_player_page.type_in_90('Też')
        add_player_page.type_in_fb('To może nie')
        add_player_page.type_in_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        add_player_page.click_submit_button()
        add_player_page.popup_located()
        add_player_page.click_main_page()
        add_player_page.screen_shot_plz('TC_05-1.png')
        dashboard_page = Dashboard(self.driver)
        #dashboard_page.title_of_page()
        dashboard_page.screen_shot_plz('TC_05-2.png')



    @classmethod
    def tearDown(self):
        self.driver.quit()
