import json
import time

import pytest
# from utils.apiBase import APIUtils
from playwright.sync_api import Playwright

from Demo.conftest import user_credentials
from Demo.pageObjects import dashboard
from Demo.pageObjects.dashboard import DashboardPage
from Demo.pageObjects.login import LoginPage

with open('C:\\Users\\pdchaudhary\\PycharmProjects\\playwrightproject'
          '\\Demo\\data\\credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web(playwright:Playwright, browserInstance, user_credentials):
    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboard = loginPage.login(userName, password)
    dashboard.selectOrder()



# @pytest.mark.parametrize('user_credentials', user_credentials_list)
# def test_select(playwright:Playwright, browserInstance, user_credentials):
#     userName = user_credentials["userEmail"]
#     password = user_credentials["userPassword"]
#     loginPage = LoginPage(browserInstance)
#     loginPage.navigate()
#     dashboard = loginPage.login(userName, password)
#     dashboard.selectcheckbox()


