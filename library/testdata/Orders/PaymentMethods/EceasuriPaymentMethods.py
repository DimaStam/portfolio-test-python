from playwright.sync_api import Page
from library.testdata.page_titles import PageTitles

class EceasuriPaymentMethods:
    # Define constants for the payment method names
    PAYU = "payU"
    BANK_TRANSFER = "bank_transfer"
    CASH_ON_DELIVERY = "cash_on_delivery"
    CARD = "card"

    # Map payment method names to their respective XPath selectors
    selectors = {
        PAYU: "//div[@class='tr payment-method payu-payment _active']//label[@for='payu_gateway']",
        BANK_TRANSFER: "//div[@class='tr']//label[@for='banktransfer']",
        CASH_ON_DELIVERY: "//div[@class='tr']//label[@for='cashondelivery']",
        CARD: "//div[@class='payment-method payu-payment']//label[@for='payu_gateway_card']",
    }

    expected_titles = {
        PAYU: PageTitles.PAYU_TITLE,
        BANK_TRANSFER: PageTitles.ZEG_SUCCESS_PAGE,
        CASH_ON_DELIVERY: PageTitles.ZEG_SUCCESS_PAGE,
        CARD: PageTitles.PAYU_TITLE,
    }

    def __init__(self, page: Page):
        self.page = page

    def select_payment_method(self, method_name):
        # Use the selectors dictionary to retrieve the XPath selector
        selector = self.selectors.get(method_name)
        if not selector:
            raise ValueError(f"Invalid payment method: {method_name}")
        self.page.click(selector)
        