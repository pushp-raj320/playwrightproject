class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self):
        self.page.get_by_role("button", name="ORDERS").click()

    def selectcheckbox(self):
        self.page.wait_for_selector("//section[@id='sidebar']/form/div[3]/div[2]/input")
        checkbox = self.page.query_selector("//section[@id='sidebar']/form/div[3]/div[2]/input")
        checkbox.click()