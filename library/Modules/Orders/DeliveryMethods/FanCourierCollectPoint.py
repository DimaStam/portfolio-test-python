from playwright.sync_api import Page

class FanCourierCollectPoints:
    def __init__(self, page: Page):
        self.page = page
        self.fan_courier_collect_points_map = page.locator("//div[@class='pointer-map fancourier-pointer-map']")
        self.address_input = page.locator("//div[@class='pointer-map fancourier-pointer-map']//input[@class='pointer-map-input pac-target-input']")
        self.search_button = page.locator("//div[@class='pointer-map fancourier-pointer-map']//a[@class='pointer-map-btn action primary']")
        self.point_pin = page.locator("//div[@role='button']")
        self.select_point_button = page.locator("//button[@class='select-machine']")

    def wait_for_fan_courier_collect_points_map(self):
        self.fan_courier_collect_points_map.wait_for(state="visible")

    def enter_delivery_point(self, address):
        self.address_input.fill(address)
        self.search_button.click()
        self.point_pin.first.wait_for()
        self.point_pin.first.click()
        self.select_point_button.click()