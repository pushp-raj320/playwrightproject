import time

from playwright.sync_api import Page

def test_playwrightBasics(playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.co.in/")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    time.sleep(5)