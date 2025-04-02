import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()