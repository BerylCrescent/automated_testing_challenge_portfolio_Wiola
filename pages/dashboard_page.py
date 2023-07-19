import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    activity_panel_xpath = "//h2[text()='Activity']"
    add_player_xpath = "//span[text()='Add player']"
    dev_team_contact_hyperlink_xpath = "//*[@target='_blank']"
    events_count_xpath = "//div[text()='Events count']"
    last_created_match_xpath = "//h6[text()='Last created match']"
    last_created_player_text_xpath = "//h6[text()='Last created player']"
    last_created_player_hyperlink_xpath = "//span[text()='Eric Forman']"
    last_updated_match_xpath = "//h6[text()='Last updated match']"
    last_updated_player_xpath = "//h6[text()='Last updated player']"
    last_updated_report_xpath = "//h6[text()='Last updated report']"
    main_page_xpath = "//span[text()='Main page']"
    matches_count_xpath = "//div[text()='Matches count']"
    players_xpath = "//span[text()='Players']"
    players_count_xpath = "//div[text()='Players count']"
    polski_language_xpath = "//span[text()='Polski']"
    reports_count_xpath = "//div[text()='Reports count']"
    scouts_panel_text_xpath = "//h6[text()='Scouts Panel']"
    scouts_panel_logo_xpath = "//div[@title='Logo Scouts Panel']"
    shortcuts_panel_xpath = "//h2[text()='Shortcuts']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    expected_title = 'Scouts panel'
    created_player = 'Eric Forman'


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.scouts_panel_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_xpath)

    def click_players(self):
        self.click_on_the_element(self.players_xpath)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)

    def activity_last_created_player(self):
        self.wait_for_element_to_be_clickable(self.scouts_panel_logo_xpath)
        #self.assert_element_text(self.driver, self.last_created_player_hyperlink_xpath, self.created_player)
        assert self.last_created_player_hyperlink_xpath == self.created_player


