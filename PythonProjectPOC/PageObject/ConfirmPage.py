from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver


    country = (By.ID, "country")
    country_name = (By.LINK_TEXT, "India")
    term_condition = (By.XPATH, "//*[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//*[@value='Purchase']")
    msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def fill_address(self):
        return self.driver.find_element(*ConfirmPage.country)

    def select_address(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def select_terms(self):
        return self.driver.find_element(*ConfirmPage.term_condition)

    def purchasebuton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def success_msg(self):
        return self.driver.find_element(*ConfirmPage.msg)