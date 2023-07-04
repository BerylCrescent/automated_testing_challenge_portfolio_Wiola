from pages.base_page import BasePage


class AddMatchForm(BasePage):
    clear_button_xpath = "//button[2][@type='button']"
    date_field_xpath = "//input[@name='date']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    league_field_xpath = "//input[@name='league']"
    main_page_xpath = "//span[text()='Main page']"
    match_at_home_button_xpath = "//label[1][@type='radio']"
    matches_xpath = "//span[text()='Matches']"
    match_out_home_button_xpath = "//label[2][@type='radio']"
    my_team_field_xpath = "//input[@name='myTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    number_field_xpath = "//input[@name='number']"
    players_xpath = "//span[text()='Players']"
    polski_language_xpath = "//span[text()='Polski']"
    rating_field_xpath = "//input[@name='rating']"
    reports_xpath = "//span[text()='Reports']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    submit_button_xpath = "//button[@type='submit']"
    tshirt_color_field_xpath = "//input[@name='tshirt']"
    pass
