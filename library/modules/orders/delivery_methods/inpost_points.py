from playwright.sync_api import Page

class InPostPoints:
    def __init__(self, page: Page):
        self.page = page
        self.inpost_map_loader = page.locator("//div[@class='loading-icon-wrapper']")
        self.summary_loader = page.locator("//div[@class='opc-block-summary _block-content-loading']//img[@alt='Loading...']")
        self.map_area = page.locator("//div[@id='widget-modal__map']//div[@id='map-leaflet']")
        self.address_input = page.locator("#easypack-search")
        self.point_dropdown = page.locator("//div[@class='inpost-search__item-list point']")
        self.search_button = page.locator("//button[@class='btn btn-search']")
        self.list_inpost_point = page.locator("//a[@href='#WRO06N']")
        self.select_delivery_point_button = page.locator("//div[@class='popup-container']//a[@class='select-link']")

    def wait_points_map(self):
        self.summary_loader.wait_for(state="hidden")
        self.map_area.wait_for(state="visible")
        self.inpost_map_loader.wait_for(state="hidden")

    def enter_delivery_point_address(self, address):
        self.address_input.clear()
        self.address_input.fill(address)
        self.point_dropdown.click()
        self.list_inpost_point.click()

    def select_delivery_point(self):
        self.select_delivery_point_button.click()