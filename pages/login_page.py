#import time


from pages.base_page import BasePage


class LoginPage(BasePage):
    language_listbox_xpath = "//form/div/div[2]/div/div"
    login_error_notification_xpath = '//form/div/div[1]/div[3]/span'
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    przypomnij_hasło_hyperlink_xpath = "//a[text()='Przypomnij hasło']"
    remind_password_hyperlink_xpath = "//a[text()='Remind password']"
    scouts_panel_text_xpath = "//form/div/div[1]/h5"
    sign_in_button_xpath = "//button[@type='submit']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'
    expected_text = 'Scouts Panel'
    expected_error = 'Identifier or password invalid.'


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    #def assert_element(self):
        #self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        #self.assert_element_text(self.driver, self.scouts_panel_text_xpath, self.expected_text)

    def screen_shot_plz(self, apngfile):
        self.assert_element_text(self.driver, self.login_error_notification_xpath, self.expected_error)
        self.driver.get_screenshot_as_file(apngfile)

    def click_on_the_remind_password(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)

    def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)
