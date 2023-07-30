import unittest


from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.add_player import TestAddPlayerPage
from test_cases.hyperlink_on_login_page_response import TestHyperlinkLoginPage
from test_cases.Log_in_log_out_test import TestLoginLogout
from test_cases.login_invalid_data import TestLoginInvalidData
from test_cases.login_to_the_system import TestLoginPage
from test_cases.remind_password_test import TestRemindPassword
from test_cases.players_test import TestPlayersSearch



def full_suite():
    test_suite = unittest.TestLoader()
    login_test = test_suite.loadTestsFromTestCase(TestLoginPage)
    add_player = test_suite.loadTestsFromTestCase(TestAddPlayerPage)
    hyperlink = test_suite.loadTestsFromTestCase(TestHyperlinkLoginPage)
    login_logout = test_suite.loadTestsFromTestCase(TestLoginLogout)
    invalid_data = test_suite.loadTestsFromTestCase(TestLoginInvalidData)
    remind_password = test_suite.loadTestsFromTestCase(TestRemindPassword)
    players_search = test_suite.loadTestsFromTestCase(TestPlayersSearch)
    return unittest.TestSuite\
        ([login_test, add_player, hyperlink, login_logout, invalid_data, remind_password, players_search])

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())