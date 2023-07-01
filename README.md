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


# Task 2 - Selectors

## Subtask 1 - New branch

- [ ] New branch

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

## Subtask 4 - Adding a new file

## Subtask 5 - Add a new file -add a match form

## Subtask 6 - Merging branches

- [ ] Branch merged
