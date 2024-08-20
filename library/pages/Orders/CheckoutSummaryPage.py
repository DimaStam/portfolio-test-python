from playwright.sync_api import Page
import allure

class CheckoutSummaryPage:

    zeg_agreement_checkbox = "#agreement__3"
    watchard_agreement_checkbox = "#agreement__6"
    hodinkovna_cz_agreement_checkbox = "#agreement__7"
    hodinkovna_sk_agreement_checkbox ="#agreement__12"
    eceasuri_agreement_checkbox = "#agreement__10"
    eorak_agreement_checkbox = "#agreement__11"
    def __init__(self, page: Page):
        self.page = page
        self.summary_area = page.locator("//div[@class='checkout__payment-method']")
        self.summary_loader = page.locator("")
        self.order_comment_button = page.locator("//button[@class='alink action action-toggle']")
        self.order_comment_input = page.locator("//textarea[@class='um-order-comment input-text order-comment order-comment-input']")
        self.place_order_button = page.locator("//button[@class='action primary w-100']")
        self.success_page_text = page.locator("//*[contains(text(), 'Dziękujemy za złożenie zamówienia!')]")
        self.payu_card_frame_locator = page.frame_locator("#payuFrame")
        self.card_number_value = "5434021016824014"
        self.card_expiry_date_value = "1229"
        self.card_cvv_code_value = "123"
        self.card_number = self.payu_card_frame_locator.frame_locator("iframe[name='_PayuFormIframe_1']").get_by_label("Card number")
        self.card_expiry_date = self.payu_card_frame_locator.frame_locator("iframe[name='_PayuFormIframe_2']").get_by_placeholder("MM / YY")
        self.card_cvv_code = self.payu_card_frame_locator.frame_locator("iframe[name='_PayuFormIframe_3']").get_by_placeholder("111")
        self.card_submit_button_zegarownia = self.payu_card_frame_locator.get_by_role("button", name="Użyj")
        self.card_submit_button_hodinkovna_cz = self.payu_card_frame_locator.get_by_role("button", name="Použít kartu")
        self.card_submit_button_hodinkovna_sk = self.payu_card_frame_locator.get_by_role("button", name="Použiť kartu")
        self.card_submit_button_watchard = self.payu_card_frame_locator.get_by_role("button", name="Use")
        self.card_submit_button_eorak = self.payu_card_frame_locator.get_by_role("button", name="Használja")
        self.card_submit_button_eceasuri = self.payu_card_frame_locator.get_by_role("button", name="Utilizați")

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

    def fill_card_fields(self, submit_button_locator):
        self.card_number.fill(self.card_number_value)
        self.card_expiry_date.fill(self.card_expiry_date_value)
        self.card_cvv_code.fill(self.card_cvv_code_value)
        submit_button_locator.click()