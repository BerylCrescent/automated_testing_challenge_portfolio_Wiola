import time


from pages.base_page import BasePage


class AddPlayer(BasePage):
    achievements_field_xpath = "//input[@name='achievements']"
    add_language_button_xpath = "//button[@aria-label='Add language']"
    add_link_yt_button_xpath = "//button[@aria-label='Add link to Youtube']"
    add_player_title_xpath = "//span[text()='Add player']"
    age_field_xpath = "//input[@name='age']"
    clear_button_xpath = "//span[text()='Clear']"
    club_field_xpath = "//input[@name='club']"
    district_field_xpath = "//input[@id='district']"
    email_field_xpath = "//input[@name='email']"
    height_field_xpath = "//input[@name='height']"
    leg_field_xpath = "//input[@id='leg']"
    level_field_xpath = "//input[@name='level']"
    main_page_xpath = "//span[text()='Main page']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    name_field_xpath = "//input[@name='name']"
    phone_field_xpath = "//input[@name='phone']"
    players_xpath = "//span[text()='Players']"
    polski_language_xpath = "//span[text()='Polski']"
    scouts_panel_text_xpath = "//h6[text()='Scouts Panel']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    submit_button_xpath = "//button[@type='submit']"
    surname_field_xpath = "//input[@name='surname']"
    web_90_field_xpath = "//input[@name='web90']"
    web_fb_field_xpath = "//input[@name='webFB']"
    web_laczy_field_xpath = "//input[@name='webLaczy']"
    weight_field_xpath = "//input[@name='weight']"
    expected_title = 'Add player'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title
