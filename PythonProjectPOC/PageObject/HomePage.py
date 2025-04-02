from selenium.webdriver.common.by import By

from PageObject.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.XPATH, '//div[@class="form-group"]/input[@name="name"]')
    email = (By.NAME, 'email')
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.ID, "exampleFormControlSelect1")
    msg_confirmation = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_check_box(self):
        return self.driver.find_element(*HomePage.checkbox)
    def submission(self):
        return self.driver.find_element(*HomePage.submit)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_confirmation(self):
        return self.driver.find_element(*HomePage.msg_confirmation)