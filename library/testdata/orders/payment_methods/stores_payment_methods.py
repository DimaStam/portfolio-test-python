from playwright.sync_api import Page
from library.testdata.page_titles import PageTitles


class StoresPaymentMethods:
    BLIK = "blik"
    PAYU = "payU"
    BANK_TRANSFER = "bank_transfer"
    CASH_ON_DELIVERY = "cash_on_delivery"
    PAYU_INSTALMENTS = "payU_instalments"
    KLARNA = "klarna"
    PAYPO = "paypo"
    TWISTO = "twisto"
    CA_INSTALLMENTS = "ca_installments"
    CARD = "card"
    PAY_PAL = "pay_pal"

    selectors = {
        BLIK: "//div[@class='row align-items-center payment-method _active']//div[@class='col-auto col-method-input']",
        PAYU: "//div[@class='col-auto col-method-input']/following-sibling::div[@class='col-auto col-method-photo']//span[@class='photo-method photo-method--payu_gateway']",
        BANK_TRANSFER: "//div[@class='tr']//label[@for='banktransfer']",
        CASH_ON_DELIVERY: "//div[@class='tr']//label[@for='cashondelivery']",
        PAYU_INSTALMENTS: "//div[@class='tr payment-method payu-payment payu-installments']//label[@for='payu_gateway_instalments']",
        KLARNA: "//div[@class='tr payment-method payu-payment klarna']",
        PAYPO: "//div[@class='tr payment-method payu-payment paypo']",
        TWISTO: "//div[@class='tr payment-method payu-payment twisto']",
        CA_INSTALLMENTS: "//div[@class='tr ca']",
        CARD: "//div[@class='payment-method-title field choice']//label[@for='payu_gateway_card']",
        PAY_PAL: "//div[@class='tr']//label[@for='paypal_express']",
    }

    expected_titles = {
        BLIK: PageTitles.PAYU_TITLE,
        PAYU: PageTitles.PAYU_TITLE,
        BANK_TRANSFER: PageTitles.STORE_1_SUCCESS_PAGE,
        CASH_ON_DELIVERY: PageTitles.STORE_1_SUCCESS_PAGE,
        PAYU_INSTALMENTS: PageTitles.PAYU_TITLE,
        KLARNA: PageTitles.PAYU_TITLE,
        PAYPO: PageTitles.PAYU_TITLE,
        TWISTO: PageTitles.PAYU_TITLE,
        CA_INSTALLMENTS: PageTitles.CA_INSTALLMENTS,
        CARD: PageTitles.PAYU_TITLE,
        PAY_PAL: PageTitles.PAYPAL_TITLE,
    }

    def __init__(self, page: Page):
        self.page = page

    def select_payment_method(self, method_name):
        selector = self.selectors.get(method_name)
        if not selector:
            raise ValueError(f"Invalid payment method: {method_name}")
        self.page.click(selector)
