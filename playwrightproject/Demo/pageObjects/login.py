
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, userName, password):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        # dashboard = DashboardPage(self.page)
        # return dashboard

    def errormsg(self):
        expect(self.page.get_by_text("Incorrect email or password.")).to_be_visible()