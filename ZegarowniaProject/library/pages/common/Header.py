from playwright.sync_api import Page
import allure
from library.pages.Orders.SearchResultPage import SearchResultPage

class Header:
    def __init__(self, page: Page):
        self.page = page
        self.main_searchbar_input = page.locator("#search")
        self.submit_search_button = page.locator("//div[@class='luigi-ac-button luigi-ac-hero-color-clickable luigi-ac-button-heromobile luigi-ac-hero-color']")

    @allure.step("Find product")
    def find_product(self, product_name):
        self.main_searchbar_input.fill(product_name)
        self.main_searchbar_input.press("Enter")
        return SearchResultPage(self.page)