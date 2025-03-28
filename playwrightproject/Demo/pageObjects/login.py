from Demo.pageObjects.dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, userName, password):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboard = DashboardPage(self.page)
        return dashboard