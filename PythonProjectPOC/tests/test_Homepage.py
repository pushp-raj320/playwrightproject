import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from testData.HomepageData import HomepageData

from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        log.info("Browser invoked")
        homepage.get_name().send_keys(getdata["name"])
        log.info(f"entering the name:{getdata["name"]}")
        homepage.get_email().send_keys(getdata["email"])
        log.info(f"entered email : {getdata["email"]}")
        homepage.get_password().send_keys(getdata["password"])
        log.info(f"password provided: {getdata["password"]}")
        homepage.get_check_box().click()
        log.info("checkbox selected")
        self.select_option_by_text(homepage.getGender(), getdata["gender"])
        log.info("gender selected")
        time.sleep(5)
        homepage.submission().click()
        output = homepage.get_confirmation().text
        log.info(f"{output}: this is the text we got")
        success_msg = "Success! The Form has been submitted successfully!"
        assert success_msg in output
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.test_homepage_data)
    def getdata(self, request):
        return request.param