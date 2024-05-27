from playwright.sync_api import Page
import allure
from library.pages.Orders.ExtraoptionsPage import ExtraoptionsPage

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_description_area = page.locator("//div[@class='product-info-main']")
        self.add_to_the_cart_button = page.locator("#product-addtocart-button")

    @allure.step("Add product to the cart")
    def add_product_to_the_cart(self):
        self.page.wait_for_load_state('networkidle')
        self.add_to_the_cart_button.click()
        return ExtraoptionsPage(self.page)