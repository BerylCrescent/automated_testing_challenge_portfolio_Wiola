<h1 align="center"> :black_nib: Wiola's challenge portfolio </h1>


### :point_right: Table of contents
1. [Task 1](#task-1---software-configuration)
2. [Task 2](#task-2---selectors)
<br>
<br>

# Task 1 - Software configuration

## Subtask 1 - Why did I choose to participate in the Dare IT Challenge?

Hello, <br>
My name is Wiola. After completing the previous challenge, [become a manual tester](https://github.com/BerylCrescent/challenge_portfolio_Wiola/tree/main), I decided it's time to take the next step and continue the journey, that started in April. <br>
I'm ready to leave, said goodbye to my family, and packed my books. I won't need the Necronomicon, but the ISTQB syllabus is necessary. It is the right weapon against bugs. Closing the door, I took one last look at the fridge *- I'll be back, my dear.* <br>
Will I meet any dragons on my way? *Only a python.* <br>
Will I get lost? *Yes, probably more than once... but isn't that the point? After all, you have to get lost in order to find yourself.* <br>
Will I manage? *Of course!*

⚔️ *Wiola*

## Subtask 2 - Fix the problem displayed on the console

- [x] Fix the problem

The following has been added to the main code:

```python
from selenium.webdriver.chrome.service import Service

```
and
```python
...
self.driver = webdriver.Chrome(service=self.driver_service)
...
```

## Subtask 3 - Adding a code to my own remote repository

- [x] Done

## Subtask 4

My test score = 12/14 points 👍
<br>
<br>
<br>


# Task 2 - Selectors

## Subtask 1 - New branch

- [x] Create a new branch - selectors

## Subtask 2 - Searching for selectors on the login page

I am testing the [Scouts test](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true) website.

+ Scouts_Panel_text_xpath

```python
- //div/h5
- //*[@id="__next"]/form/div/div[1]/h5     shorter version ➡️     //form/div/div[1]/h5
- //*[text()="Scouts Panel"]
```
  
+ Login_field_xpath

```python
- //*[text()="Login"]
- //input[@id="login"]     shorter version ➡️     //*[@id="login"]
- //input[@name="login"]
- //*[@for="login"]
```
  
+ Password_field_xpath

```python
- //input[@type="password"]
- //input[@id="password"]     shorter version ➡️     //*[@id="password"]
- //input[@name="password"]
- //*[text()="Password"]
- //*[@for="password"]
```

+ Remind_password_hyperlink_xpath

```python
- //a[text()="Remind password"]
- //*[*id="__next"]/form/dividiv[1]/a     shorter version ➡️     //form/div/div[1]/a
- //*[contains(@class, "jss4")]
```
  
+ Language_listbox_xpath

```python
- //*[text()="English"]
- //*[@id="__next"]/form/div/div[2]/div/div     shorter version ➡️     //form/div/div[2]/div/div
- //*[contains(@class, "MuiSelect-root")]
```
+ Sign_in_button_xpath

```python
- //*[text()="Sign in"]
- //button[@type="submit"]
- //*[@id="__next"]/form/div/div[2]/button     shorter version ➡️     //form/div/div[2]/button 
- //*[contains(@class, "MuiButton-label")]
```

## Subtask 3 - Adding selectors to a project

The following selectors were added to login_page.py:

```python
login_field_xpath = "//*[@id='login']"
password_field_xpath = "//*[@id='password']"
sign_in_button_xpath = "//button[@type='submit']"
language_listbox_xpath = "//form/div/div[2]/div/div"
remind_password_hyperlink_xpath = "//a[text()='Remind password']"
scouts_panel_text_xpath = "//form/div/div[1]/h5"
```


## Subtask 4 - Adding a new file

A new file named Dashboard.py was created.
The task was to add at leats 10 selectors - I have 19, just for practice purpose. <br>
The following selectors were added:

```python
from pages.base_page import BasePage


class Dashboard(BasePage):
    activity_panel_xpath = "//h2[text()='Activity']"
    add_player_xpath = "//span[text()='Add player']"
    dev_team_contact_hyperlink_xpath = "//*[@target='_blank']"
    events_count_xpath = "//div[text()='Events count']"
    last_created_match_xpath = "//h6[text()='Last created match']"
    last_created_player_xpath = "//h6[text()='Last created player']"
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
    pass

```

## Subtask 5 - Add a new file - add a match form

A new file named add_match_form.py was created.
The task was to add at leats 10 selectors - like previously, I have 19. <br>
The following selectors were added:

```python
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
```

## Subtask 6 - Merging branches

- [x] Branch merged

<br>
<br>
<br>
