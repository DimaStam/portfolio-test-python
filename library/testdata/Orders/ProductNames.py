from playwright.sync_api import Page

class ProductNames:
    product_name = "Timex Classic Southview TW2T35100"

    def __init__(self, page: Page):
        self.page = page