from playwright.sync_api import Page
from library.pages.user.my_account_page import MyAccountPage
from faker import Faker
import allure
import time


class CreateAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname = page.locator("#firstname")
        self.lastname = page.locator("#lastname")
        self.email_address = page.locator("#email_address")
        self.password = page.locator("#password")
        self.confirm_password = page.locator("//input[@name='password_confirmation']")
        self.create_account_button = page.locator("//button[@class='action submit primary']")

    @allure.step("Fill main register form")
    def fill_main_register_form(self):
        fake = Faker()
        password = "TheBestPassword1234!"
        self.firstname.fill(fake.name())
        self.lastname.fill(fake.last_name())
        self.email_address.fill(str(round(time.time()) * 1000) + "@gmail.com")
        self.password.fill(password)
        self.confirm_password.fill(password)
        return self

    @allure.step("Click create accounf button")
    def click_create_account_button(self):
        self.create_account_button.click()
        return MyAccountPage(self.page)
