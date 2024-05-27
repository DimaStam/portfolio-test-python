from playwright.sync_api import Page
import allure
from library.pages.user.MyAccountPage import MyAccountPage

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_form = page.locator("#login-block")
        self.input_user_name = page.locator("#email")
        self.input_password = page.locator("#pass")
        self.login_button = page.locator("//button[@class='action login primary']")

    @allure.step("Wait for login page")
    def wait_for_login_page(self):
        self.login_form.wait_for(timeout=15000)
        return self
    
    @allure.step("Login to system")
    def login_to_system(self, username, password):
        self.fill_login_form(username, password)
        self.click_login_button()
        return MyAccountPage(self.page)
    
    @allure.step("Fill login form")
    def fill_login_form(self, username, password):
        self.input_user_name.fill(username)
        self.input_password.fill(password)
        return self
    
    @allure.step("Click login button")
    def click_login_button(self):
        self.login_button.click()
        return self