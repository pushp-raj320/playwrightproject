from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver


    products = (By.XPATH, "//div[@class='card h-100']" )
    products_add_cart = (By.XPATH, "div/button")
    products_name = (By.XPATH, "div/h4/a")
    check_out_button = (By.XPATH, "//div[@id='navbarResponsive']//a" )
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")



    def get_products(self):
        return self.driver.find_elements(*CheckOutPage.products)


    def get_products_add_cart(self):
        return self.driver.find_element(*CheckOutPage.products_add_cart)

    def get_check_out(self):
        return self.driver.find_element(*CheckOutPage.check_out_button)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

