from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    language_listbox_xpath = "//form/div/div[2]/div/div"
    remind_password_hyperlink_xpath = "//a[text()='Remind password']"
    scouts_panel_text_xpath = "//form/div/div[1]/h5"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
