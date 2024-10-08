from playwright.sync_api import Page

class PaymentMethods:

    blik = "//div[@class='row align-items-center payment-method _active']"
    payU = "//div[@class='tr payment-method payu-payment']//label[@for='payu_gateway']"
    bank_transfer = "//div[@class='tr']//label[@for='banktransfer']"
    cash_on_delivery = "//div[@class='tr']//label[@for='cashondelivery']"
    payU_instalments = "//div[@class='tr payment-method payu-payment payu-installments']//label[@for='payu_gateway_instalments']"
    klarna = "//div[@class='tr payment-method payu-payment klarna']"
    paypo = "//div[@class='tr payment-method payu-payment paypo']"
    twisto = "//div[@class='tr payment-method payu-payment twisto']"
    ca_installments = "//div[@class='tr ca']"
    card = "//div[@class='payment-method-title field choice']//label[@for='payu_gateway_card']"
    pay_pal = "//div[@class='tr']//label[@for='paypal_express']"

    eorak_card = "//div[@class='payment-method payu-payment _active']//label[@for='payu_gateway_card']"

    def __init__(self, page: Page):
        self.page = page
        