from playwright.sync_api import Page
import allure
from library.pages.orders.checkout_shipping_page import CheckoutShippingPage


class StepLoginFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_loader = page.locator("//img[@alt='Ładuję...']")
        self.login_step = page.locator("//div[@class='row login_step']")
        self.buy_as_guest_button = page.locator("//input[@class='action continue primary']")

    @allure.step("Wait for step login form page")
    def wait_for_step_login_form_page(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.checkout_loader.wait_for(state="hidden", timeout=15000)
        self.login_step.wait_for()

    @allure.step("Select 'Buy as guest user'")
    def select_buy_as_guest_user(self):
        self.buy_as_guest_button.click()
        return CheckoutShippingPage(self.page)
