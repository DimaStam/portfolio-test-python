from playwright.sync_api import Page
import allure
from library.modules.orders.add.shipping_form_data import ShippingForm
from library.pages.orders.checkout_summary_page import CheckoutSummaryPage
from library.modules.orders.delivery_methods.inpost_points import InPostPoints
from library.modules.orders.delivery_methods.dhl_pop_points import DHLPOPPoints


class CheckoutShippingPage:
    default_data = ShippingForm(
        user_email="test1testt@gmail.com",
        user_first_name="Dima",
        user_last_name="Tester",
        street_address="Testowa",
        house_number="7a",
        post_code="53332",
        city="Wrocław",
        phone_number="555555555")

    def __init__(self, page: Page):
        self.page = page
        self.inpost_points = InPostPoints(page)
        self.dhl_pop_points = DHLPOPPoints(page)
        self.dhl_select_point_button = page.locator("//button[@id='dhllink']")
        self.shipping_methods_loader = page.locator("//li[@id='opc-shipping_method']//div[@class='loading-mask']")
        self.shipping_form = page.locator("//li[@class='checkout-shipping-address']")
        self.proceed_to_summary_button = page.locator("#summary-shipping-button")
        self.user_email_input = page.locator("//li[@class='checkout-shipping-address']//input[@id='customer-email']")
        self.phone_number_input = page.locator("//input[@name='telephone']")
        self.user_first_name_input = page.locator("//input[@name='firstname']")
        self.user_last_name_input = page.locator("//input[@name='lastname']")
        self.street_address_input = page.locator("//input[@name='street[0]']")
        self.house_number_input = page.locator("//input[@name='street[1]']")
        self.post_code_input = page.locator("//input[@name='postcode']")
        self.city_input = page.locator("//input[@name='city']")

    @allure.step("Fill shipping form")
    def fill_shipping_form(self, data: ShippingForm = None):
        data = data or self.default_data
        self.page.wait_for_load_state('networkidle')
        self.user_email_input.wait_for(state="visible")
        self.user_email_input.fill(data.user_email)
        self.user_first_name_input.fill(data.user_first_name)
        self.user_last_name_input.fill(data.user_last_name)
        self.street_address_input.fill(data.street_address)
        self.house_number_input.fill(data.house_number)
        self.post_code_input.fill(data.post_code)
        self.city_input.fill(data.city)
        self.phone_number_input.fill(data.phone_number)

    @allure.step("Select delivery method")
    def select_delivery_method(self, delivery_method: str):
        self.page.wait_for_load_state('networkidle')
        self.page.locator(delivery_method).click()

    @allure.step("Select InPost delivery point")
    def select_inpost_delivery_point(self):
        self.inpost_points.wait_points_map()
        self.inpost_points.enter_delivery_point_address("WRO06N")
        self.inpost_points.select_delivery_point()

    @allure.step("Select DHL POP delivery point")
    def select_dhl_pop_delivery_point(self):
        self.dhl_select_point_button.wait_for(state='attached')
        self.page.wait_for_load_state('networkidle')
        self.dhl_pop_points.wait_dhl_points_map()
        self.dhl_pop_points.enter_delivery_point_address("Pabianicka 10, Wrocław")

    @allure.step("Proceed tu summary page")
    def proceed_to_summary(self) -> CheckoutSummaryPage:
        self.page.wait_for_load_state('networkidle')
        self.proceed_to_summary_button.click()
        return CheckoutSummaryPage(self.page)
