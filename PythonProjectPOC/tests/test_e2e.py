import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckoutPage import CheckOutPage
from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):


    def test_e2e(self, setup):

        log = self.get_logger()
        homepage = HomePage(self.driver)
        check_out_page = homepage.shopItems()
        log.info("getting all item name")
        products = check_out_page.get_products()
        # confirmpage = ConfirmPage(self.driver)

        for product in products:

            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                check_out_page.get_products_add_cart().click()

        check_out_page.get_check_out().click()
        confirmpage = check_out_page.checkOutItems()
        log.info("Entering country name")
        confirmpage.fill_address().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.select_address().click()
        confirmpage.select_terms().click()
        confirmpage.purchasebuton().click()
        succ_msg = confirmpage.success_msg().text
        log.info(f"{succ_msg} : getting success msg")

        assert "Success" in succ_msg