import time

from pages.base_page import BasePage

from selenium.webdriver import ActionChains


class PlayersPage(BasePage):
    columns_age_box_xpath = "//*[@value='age']"
    columns_close_button_xpath = "//body/div[2]/div[3]/button"
    columns_club_box_xpath = "//*[@value='club']"
    columns_main_position_box_xpath = "//*[@value='mainPosition']"
    columns_matches_box_xpath = "//*[@value='matches']"
    columns_name_box_xpath = "//*[@value='name']"
    columns_rating_box_xpath = "//*[@value='rating']"
    columns_reports_box_xpath = "//*[@value='reports']"
    columns_surname_box_xpath = "//*[@value='surname']"
    download_csv_button_xpath = "//*[@title='Download CSV']"
    filters_age_max_field_xpath = "//div[2]/div[3]/div/div/div/div[2]/div/input"
    filters_age_min_field_xpath = "//div[2]/div[3]/div/div/div/div[1]/div/input"
    filters_club_field_xpath = "//div[2]/div[5]/div/div/div/input"
    filters_close_button_xpath = "/html/body/div[2]/div[3]/button"
    filters_main_position_field_xpath = "//div[2]/div[4]/div/div/div/input"
    filters_name_field_xpath = "//div[2]/div[1]/div/div/div/input"
    filters_rate_max_field_xpath = "//div[6]/div/div/div/div[2]/div/input"
    filters_rate_min_field_xpath = "//div[6]/div/div/div/div[1]/div/input"
    filters_search_button_xpath = "//main/div[2]/div/div/div[2]/div"
    filters_surname_field_xpath = "//div/div[2]/div[2]/div/div/div/input"
    filters_table_button_xpath = "//*[@title='Filter Table']"
    main_page_xpath = "//span[text()='Main page']"
    next_page_button_xpath = "//*[@id='pagination-next']"
    scouts_panel_text_xpath = "//h6[text()='Scouts Panel']"
    search_field_xpath = "//input[1]"
    polski_language_xpath = "//span[text()='Polski']"
    previous_page_button_xpath = "//*[@id='pagination-back']"
    print_button_xpath = "//*[@aria-label='Print']"
    reset_filters_xpath = "//*[@aria-label='RESET']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    table_age_xpath = "//div/div[text()='Age']"
    table_club_xpath = "//div/div[text()='Club']"
    table_close_xpath = "/html/body/div[2]/div[3]/button"
    table_main_position_xpath = "//div/div[text()='Main position']"
    table_matches_xpath = "//th/div[text()='Matches']"
    table_name_xpath = "//div/div[text()='Name']"
    table_surname_xpath = "//div/div[text()='Surname']"
    table_rating_xpath = "//div/div[text()='Rating']"
    table_reports_xpath = "//th/div[text()='Reports']"
    view_columns_button_xpath = "//*[@title='View Columns']"
    #players_page_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    players_page_url = 'https://dareit.futbolkolektyw.pl/en/players'
    expected_title = "Players"


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        assert self.get_page_title(self.players_page_url) == self.expected_title

    def search_name(self, name):
        self.wait_for_element_to_be_clickable(self.search_field_xpath)
        self.field_send_keys(self.search_field_xpath, name)

    def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)

    def fill_filter_table(self, name, surname, main_position, club):
        self.click_on_the_element(self.filters_table_button_xpath)
        self.field_send_keys(self.filters_name_field_xpath, name)
        self.field_send_keys(self.filters_surname_field_xpath, surname)
        self.field_send_keys(self.filters_main_position_field_xpath, main_position)
        self.field_send_keys(self.filters_club_field_xpath, club)
        self.click_on_the_element(self.filters_close_button_xpath)
        self.wait_for_element_to_be_clickable(self.filters_search_button_xpath)

    def choose_columns(self):
        self.click_on_the_element(self.view_columns_button_xpath)
        self.click_on_the_element(self.columns_age_box_xpath)
        self.click_on_the_element(self.columns_rating_box_xpath)
        self.click_on_the_element(self.columns_matches_box_xpath)
        self.click_on_the_element(self.columns_reports_box_xpath)
        self.click_on_the_element(self.columns_close_button_xpath)
        self.click_on_the_element(self.search_field_xpath)