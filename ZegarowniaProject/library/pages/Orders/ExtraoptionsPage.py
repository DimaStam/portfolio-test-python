from playwright.sync_api import Page
import allure
from library.pages.Orders.CheckoutCartPage import CheckoutCartPage

class ExtraoptionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_cart_button = page.locator("//a[@class='action primary checkout arrowed w-100']")
        self.extraoptions_area = page.locator("//div[@class='row extra-options__wrapper']")
    
    @allure.step("Navigate to the checkout cart page")
    def navigate_to_the_checkout_cart(self):
        # self.page.wait_for_load_state('networkidle')
        self.page.wait_for_load_state("domcontentloaded")
        self.checkout_cart_button.click()
        return CheckoutCartPage(self.page)
        