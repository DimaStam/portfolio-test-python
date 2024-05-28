from playwright.sync_api import Page

class DHLPOPPoints:
    def __init__(self, page: Page):
        self.page = page
        self.iframe_dhl = page.frame_locator("internal:role=dialog[name=\"Mapa Parcelshop\"i] >> iframe").frame_locator("iframe >> nth=0")
        self.map_searchbar = self.iframe_dhl.get_by_placeholder("wpisz ulicę, nr, miasto")
        self.search_button = self.iframe_dhl.locator("#adrsubmit")
        self.point_name = self.iframe_dhl.get_by_text("DHL POP Kaufland punkt")
        self.select_point_button = self.iframe_dhl.get_by_role("button", name="Wybieram ten")

    def enter_delivery_point_address(self, address):
        self.map_searchbar.fill(address)
        self.search_button.click()
        self.point_name.click()
        self.select_point_button.click()

    def wait_dhl_points_map(self):
        self.map_searchbar.wait_for()