from playwright.sync_api import Page
import allure

class CheckoutSummaryPage:

    zeg_agreement_checkbox = "#agreement__3"
    watchard_agreement_checkbox = "#agreement__6"
    hodinkovna_cz_agreement_checkbox = "#agreement__7"
    hodinkovna_sk_agreement_checkbox ="#agreement__12"
    eceasuri_agreement_checkbox = "#agreement__10"
    def __init__(self, page: Page):
        self.page = page
        self.summary_area = page.locator("//div[@class='checkout__payment-method']")
        self.summary_loader = page.locator("")
        self.order_comment_button = page.locator("//button[@class='alink action action-toggle']")
        self.order_comment_input = page.locator("//textarea[@class='um-order-comment input-text order-comment order-comment-input']")
        self.place_order_button = page.locator("//button[@class='action primary w-100']")
        self.success_page_text = page.locator("//*[contains(text(), 'Dziękujemy za złożenie zamówienia!')]")

    @allure.step("Select payment method")
    def select_payment_method(self, payment_method):
        self.page.locator(payment_method).click()

    @allure.step("Add order comment")
    def add_order_comment(self):
        self.order_comment_button.click()
        self.order_comment_input.clear()
        self.order_comment_input.fill("Testowe zamówienie G4N")

    @allure.step("Select agreement checkbox")
    def select_agreement_checkbox(self, store_agreement):
        self.page.locator(store_agreement).click()
    
    @allure.step("Place order")
    def place_order(self):
        self.place_order_button.click()

    