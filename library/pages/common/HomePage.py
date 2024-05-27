from playwright.sync_api import Page
from library.pages.user.LoginPage import LoginPage
import allure

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.main_header = page.locator("//header[@class='page-header']")
        self.customer_account_icon = page.locator("//div[@class='header__account col']")

    @allure.step("Wait for home page")
    def wait_for_home_page(self):
        self.main_header.wait_for(timeout=15000)
        return self
    
    @allure.step("Navigate to the login page")
    def navigate_to_login_page(self):
        self.customer_account_icon.click()
        return LoginPage(self.page)