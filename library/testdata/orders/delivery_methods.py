from playwright.sync_api import Page


class DeliveryMethods:
    courier_dhl = "//tr[@class='method--courier_dhl_dhl24pl']"
    dhl_pop = "//tr[@class='method--parcelshop_dhl_dhl24pl']//td[@class='col-method']"
    inpost = "//tr[@class='method--inpost_inpost']//td[@class='col-method-input']"
    ups_standard = "//tr[@class='method--bestway_tablerate']"
    free_shipping_saloon = "//tr[@class='method--shipping_premium_shipping_premium']//td[@class='col-method-input']"
    fre_shipping_point = "//tr[@class='method--freeshipping_freeshipping']//td[@class='col-method-input']"

    def __init__(self, page: Page):
        self.page = page
