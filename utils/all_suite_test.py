import unittest


from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.add_player import TestAddPlayerPage
from test_cases.hyperlink_on_login_page_response import TestHyperlinkLoginPage
from test_cases.Log_in_log_out_test import TestLoginLogout
from test_cases.login_invalid_data import TestLoginInvalidData
from test_cases.login_to_the_system import TestLoginPage



def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestAddPlayerPage))
    test_suite.addTest(makeSuite(TestHyperlinkLoginPage))
    test_suite.addTest(makeSuite(TestLoginLogout))
    test_suite.addTest(makeSuite(TestLoginInvalidData))
    test_suite.addTest(makeSuite(TestLoginPage))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())