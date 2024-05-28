from playwright.sync_api import Page

class DeliveryMethods:
    # Define constants for the delivery method names
    COURIER_DHL = "courier_dhl"
    DHL_POP = "dhl_pop"
    INPOST = "inpost"
    UPS_STANDARD = "ups_standard"
    FREE_SHIPPING_ZEG_SALOON = "free_shipping_zeg_saloon"
    FRE_SHIPPING_ZEG_POINT = "fre_shipping_zeg_point"

    # Map delivery method names to their respective XPath selectors
    selectors = {
        COURIER_DHL: "//tr[@class='method--courier_dhl_dhl24pl']",
        DHL_POP: "//tr[@class='method--parcelshop_dhl_dhl24pl']",
        INPOST: "//tr[@class='method--inpost_inpost']//td[@class='col-method-input']",
        UPS_STANDARD: "//tr[@class='method--bestway_tablerate']",
        FREE_SHIPPING_ZEG_SALOON: "//tr[@class='method--shipping_premium_shipping_premium']//td[@class='col-method-input']",
        FRE_SHIPPING_ZEG_POINT: "//tr[@class='method--freeshipping_freeshipping']//td[@class='col-method-input']",
    }

    def __init__(self, page: Page):
        self.page = page

    def select_delivery_method(self, method_name):
        # Use the selectors dictionary to retrieve the XPath selector
        selector = self.selectors.get(method_name)
        if not selector:
            raise ValueError(f"Invalid delivery method: {method_name}")
        self.page.click(selector)
        