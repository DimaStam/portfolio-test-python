from playwright.sync_api import Page
import allure
from library.pages.common.ProductPage import ProductPage

class SearchResultPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_tile = page.locator("//div[@id='product-list']//li[@class='item product product-item']").first

    @allure.step("Select product")
    def select_product(self):
        self.product_tile.click()
        return ProductPage(self.page)

    