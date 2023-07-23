<h1 align="center"> :black_nib: Wiola's challenge portfolio </h1>


### :point_right: Table of contents
1. [Task 1](#task-1---software-configuration)
2. [Task 2](#task-2---selectors)
3. [Task 3](#task-3---first-test-and-assert)
4. [Task 4](#task-4---refactoring-debugger-and-test-cases)
5. [Task 5](#task-5---robot-framework)
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

# Task 3 - First test and assert

Assertion exercise record avaliable [here](https://drive.google.com/file/d/1BBMni_vzRzv2dJ4oQUMGR1-Scl8uCBT2/view?usp=sharing)

## Subtask 1 - Completing the login page

The login_page.py file was updated by adding the following methods:

```python

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
```

## Subtask 2 - A new test case

Subtask 2 record avaliable [here](https://drive.google.com/file/d/1a0NV3_SBnXTsitIahK0xjYFoxPggTQbH/view?usp=sharing) <br>
The login_to_the_system.py file was created. I used the following script:

```python
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

```

Also, this tricky bastard was added:

```python
from pages.login_page import LoginPage
```

Test passed - the methods filled in the proper fields, therefore we were logged in and could see the dashboard.

## Subtask 3 - Assert

Subtask 3 record avaliable [here](https://drive.google.com/file/d/1uZijXXpaqzvjtxBFaG1kbbwwufd6bLTo/view?usp=sharing)
<br>

The following was added to BasePage:
```python
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title
```

Is dashboard title and login page correct?
Test passed - the assertion returned true.



## Subtask 4 - Repeating what we already know

Subtask 4 record avaliable [here](https://drive.google.com/file/d/12Z0AuWspXl2e_QFJUEKJJxITODsnjCoG/view?usp=sharing)
<br>

For this task, add_player_page.py and add_player.py test were created. <br>
The test passed - the assertion returned true.


## Subtask 5 - Optional task

Subtask 5 record avaliable [here](https://drive.google.com/file/d/1_ux3eFw6md3jmPlcboA6Hvt_7xKCQ9L9/view?usp=sharing)
<br>
The test failed because self.scouts_panel_text_xpath != self.expected_text

My solution in login_page.py

```python
def assert_element(self):
        time.sleep(1)
        self.assert_element_text(self.driver, self.scouts_panel_text_xpath, self.expected_text)
```

And in login_to_the_system.py test:

```python
user_login.assert_element()
```
<br>

The test failed because there happened to be an error in the subtask, a typo - expected_text was 'Scout Panel' insted of 'Scouts Panel'. <br>
The test passed after correcting the typo.<br>
Record avaliable [here](https://drive.google.com/file/d/1NP7kZW5NVVKaejFjs0LZYyqi-T1DFf6B/view?usp=sharing)


<br>
<br>

# Task 4 - Refactoring, debugger and test cases

In this task, I created test cases and automated tests for them. <br>
Prework recording with wait method added avaliable [here](https://drive.google.com/file/d/116vlCvjttaf5d7gcS0IHmrBO0B4lloJd/view?usp=sharing)

## Subtask 1 - Writing test cases

[Link](https://docs.google.com/spreadsheets/d/148mOoML0UUtxGtexcV5bTFZzoWZsKeKl/edit?usp=sharing&ouid=100493076818843703891&rtpof=true&sd=true) to the test cases prepared for this task - 7 in total.

## Subtask 2 - Writing code based on test cases

- [x] The code was written

## Subtask 3 - Adding recordings from tests to Google Drive

Recordings prepared for this task:
- [Test Case 1](https://drive.google.com/file/d/1vMC6wUgpvaIHDovrfzftQKAAKKPP9lcI/view?usp=sharing)
- [Test Case 2](https://drive.google.com/file/d/1q83psKzicdMGDT88wC1P5SFxcQEqEYnQ/view?usp=sharing)
- [Test Case 3](https://drive.google.com/file/d/1851OgslSgySbXNMcFlehgmyhVh7MHWWp/view?usp=sharing)
- [Test Case 4](https://drive.google.com/file/d/1t_6ZJ8wA5GZCBNjAExkTA0v9VfU57iQT/view?usp=sharing)
- [Test Case 5](https://drive.google.com/file/d/1A4QKa-sk907olZ-KQ4kiJIPVHiavcg0D/view?usp=sharing)
- [Test Case 6](https://drive.google.com/file/d/1ln3QOPUo6HTsXxvl72t0rM4CkYtQsgHo/view?usp=sharing)
- [Test Case 7](https://drive.google.com/file/d/1Pt6iueaahUNCJA8Hpz4tkGa9gp42ZRYe/view?usp=sharing)


## Subtask 4 - Screenshot method and test report - for volunteers and groups

Reports (.html) avaliable [here](https://drive.google.com/drive/folders/1Hc0N68ikJ8-p49pe77dPGQJ8_LobaWUp?usp=drive_link).
When opened by Google Docs, the file looks decent, however I prefer the browser:
- Report TC_01 [screenshot](https://drive.google.com/file/d/1YtePXbh7_npB1xKj925y11Slyn6JLWFp/view?usp=drive_link)
- Report TC_02 [screenshot](https://drive.google.com/file/d/1BkoOy6PxpBix_niGPn85-1CcEU8I4411/view?usp=drive_link)
- Report TC_03 [screenshot](https://drive.google.com/file/d/1wdHb49U_R1yLdLXZG4yj3MsG8ANqVR05/view?usp=drive_link)
- Report TC_04 [screenshot](https://drive.google.com/file/d/1GRE9ABF6xYyh18QG4e8pjYa3uf4S_s6M/view?usp=drive_link)
- Report TC_05 [screenshot](https://drive.google.com/file/d/1uoWxAhQ0ZgeL3soUsbSgB_n88RSdDqdp/view?usp=drive_link)
- Report TC_06 [screenshot](https://drive.google.com/file/d/1jhuGzJH9rUOYk2nAHRguCzgYGoN85H9l/view?usp=drive_link)
- Report TC_07 [screenshot](https://drive.google.com/file/d/1WkNu5use4Ii0L2UKLmlbjnH11fPxgnYA/view?usp=drive_link)

As for the screenshot method - the following code was added:

```python

def screen_shot_plz(self, apngfile):
        self.driver.get_screenshot_as_file(apngfile)

```

## Subtask 5 - For volunteers - if else construction

Time is my sworn enemy, but I will succeed ⚔️
This subtask will not stay empty for too long

<br>
<br>

# Task 5 - Robot Framework

- [x] Create a new [repository](https://github.com/BerylCrescent/ScoutsTest_robotframework/tree/main)
- [x] All tests from previous projects have been rewritten to Robot Framework

## Subtask 1

This subtask is avaliable in the new repository. </br>
Test records are avaliable [here](https://drive.google.com/drive/folders/1oh-bwt7Y9L9SIPH4Z8QN_vzt3XYTJRNq?usp=sharing)




