import time



from pages.base_page import BasePage


class AddPlayer(BasePage):
    achievements_field_xpath = "//input[@name='achievements']"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_language_button_xpath = "//button[@aria-label='Add language']"
    add_language_input_xpath = "//input[@name='languages[0]']"
    add_link_yt_button_xpath = "//button[@aria-label='Add link to Youtube']"
    add_link_yt_input_xpath = "//input[@name='webYT[0]']"
    add_player_title_xpath = "//span[text()='Add player']"
    age_field_xpath = "//input[@name='age']"
    clear_button_xpath = "//span[text()='Clear']"
    club_field_xpath = "//input[@name='club']"
    district_field_xpath = "//*[@id='mui-component-select-district']"
    district_field_dolnoslaskie_xpath = "//li[@data-value='dolnoslaskie']"
    email_field_xpath = "//input[@name='email']"
    height_field_xpath = "//input[@name='height']"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    leg_field_left_xpath = "//div/ul/li[@data-value='left']"
    leg_field_right_xpath = "//li[@data-value='right']"
    level_field_xpath = "//input[@name='level']"
    main_page_xpath = "//span[text()='Main page']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    name_field_xpath = "//input[@name='name']"
    notification_redirect_eng_xpath = "//*[text()='Redirect to edit page']"
    notification_saved_eng_xpath = "//*[text()='Added player.']"
    phone_field_xpath = "//input[@name='phone']"
    players_xpath = "//span[text()='Players']"
    polski_language_xpath = "//span[text()='Polski']"
    saved_player_notification_xpath = "//*[@id='isvegkkxq2']/div[1]"
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


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_second_position(self, second):
        self.field_send_keys(self.second_position_field_xpath, second)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)

    def click_main_page(self):
        self.click_on_the_element(self.main_page_xpath)

    def click_leg_select(self):
        self.click_on_the_element(self.leg_field_xpath)
        self.click_on_the_element(self.leg_field_left_xpath)

    def click_district_select(self):
        self.click_on_the_element(self.district_field_xpath)
        self.click_on_the_element(self.district_field_dolnoslaskie_xpath)

    def popup_located(self):
        self.visibility_of_element_located(self.notification_saved_eng_xpath)
        self.visibility_of_element_located(self.notification_redirect_eng_xpath)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_achievements(self, ach):
        self.field_send_keys(self.achievements_field_xpath, ach)

    def type_in_language(self, lang):
        self.click_on_the_element(self.add_language_button_xpath)
        self.field_send_keys(self.add_language_input_xpath, lang)

    def type_in_laczy(self, laczy):
        self.field_send_keys(self.web_laczy_field_xpath, laczy)

    def type_in_90(self, web_90):
        self.field_send_keys(self.web_90_field_xpath, web_90)

    def type_in_fb(self, fb):
        self.field_send_keys(self.web_fb_field_xpath, fb)

    def type_in_youtube(self, rickroll):
        self.click_on_the_element(self.add_link_yt_button_xpath)
        self.field_send_keys(self.add_link_yt_input_xpath, rickroll)


