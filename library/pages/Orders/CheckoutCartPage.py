from playwright.sync_api import Page
import allure
from library.pages.Orders.StepLoginFormPage import StepLoginFormPage

class CheckoutCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.go_to_order_button = page.locator("//button[@class='action primary arrowed checkout']")
        self.checkout_cart_area = page.locator("//div[@class='row cart-container']")

    @allure.step("Navigate to the step login form")
    def navigate_to_the_step_login_form_page(self):
        self.page.wait_for_load_state('networkidle')
        self.go_to_order_button.click()
        return StepLoginFormPage(self.page)