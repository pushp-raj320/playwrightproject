class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self):
        self.page.get_by_role("button", name="ORDERS").click()

    def selectcheckbox(self):
        self.page.locator("//label[text()='fashion']/preceding-sibling::input[@type='checkbox']").check()