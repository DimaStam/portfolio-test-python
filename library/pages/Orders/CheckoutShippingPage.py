from playwright.sync_api import Page
import allure
from library.Modules.Orders.Add.ShippingFormData import ShippingForm
from library.pages.Orders.CheckoutSummaryPage import CheckoutSummaryPage
from library.Modules.Orders.DeliveryMethods.InPostPoints import InPostPoints
from library.Modules.Orders.DeliveryMethods.DHLPOPPoints import DHLPOPPoints
from library.Modules.Orders.DeliveryMethods.BalikovnaPoints import BalikovnaPoints
from library.Modules.Orders.DeliveryMethods.BalikNaPostuPoints import BalikNaPostuPoints
from library.Modules.Orders.DeliveryMethods.BalikoboxPoints import BalikoboxPoints
from library.Modules.Orders.DeliveryMethods.SpsParcelshopPoints import SpsParcelshopPoints
from library.Modules.Orders.DeliveryMethods.FanCourierCollectPoint import FanCourierCollectPoints
import time

class CheckoutShippingPage:
    default_data = ShippingForm(
            user_email="global1Autotest@gmail.com",
            user_first_name="Dima",
            user_last_name="Tester",
            street_address="Powstańców Śląskich",
            house_number="7a",
            post_code="53332",
            city="Wrocław",
            phone_number="555555555")

    def __init__(self, page: Page):
        self.page = page
        self.inpost_points = InPostPoints(page)
        self.dhl_pop_points = DHLPOPPoints(page)
        self.balikovna_points = BalikovnaPoints(page)
        self.balik_na_postu_points = BalikNaPostuPoints(page)
        self.balikobox_points = BalikoboxPoints(page)
        self.sps_parcelshop_points = SpsParcelshopPoints(page)
        self.fan_courier_delivery_points = FanCourierCollectPoints(page)
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
        if data is None:
            data = self.default_data
        self.page.wait_for_load_state('networkidle')
        # self.page.wait_for_load_state("domcontentloaded")
        # self.page.expect_response(lambda response: "totals-information" in response.url and response.status == 200)
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
        # self.page.expect_response(lambda response: "totals-information" in response.url and response.status == 200)
        # time.sleep(2)
        self.page.wait_for_load_state('networkidle')
        # self.page.expect_response(lambda response: "totals-information" in response.url and response.status == 200)
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
        # self.dhl_select_point_button.click()
        self.dhl_pop_points.wait_dhl_points_map()
        self.dhl_pop_points.enter_delivery_point_address("Pabianicka 10, Wrocław")

    @allure.step("Select Balikovna delivery point")
    def select_balikovna_delivery_point(self):
        self.balikovna_points.wait_for_balikovna_points_map()
        self.balikovna_points.enter_delivery_point("Česká pošta, Kojčice, Česko")

    @allure.step("Select Balik na postu delivery point")
    def select_balik_na_postu_delivery_point(self):
        self.balik_na_postu_points.wait_for_balik_na_postu_points_map()
        self.balik_na_postu_points.enter_delivery_point("Česká pošta, Kojčice, Česko")

    @allure.step("Select Balikobox delivery point")
    def select_balikobox_delivery_point(self):
        self.balikobox_points.wait_for_balik_na_postu_points_map()
        self.balikobox_points.enter_delivery_point("Plynárenská 7a, Ružinov, Slovensko")

    def select_sps_parcelshop_delivery_point(self):
        self.sps_parcelshop_points.wait_for_balik_na_postu_points_map()
        self.sps_parcelshop_points.enter_delivery_point("Plynárenská 7a, Ružinov, Slovensko")

    @allure.step("Select Fan Courier Collect Point")
    def select_fan_courier_collect_point(self):
        self.fan_courier_delivery_points.wait_for_fan_courier_collect_points_map()
        self.fan_courier_delivery_points.enter_delivery_point("Strada Ferdinand nr. 38A, Râmnicu Vâlcea, România")

    @allure.step("Proceed tu summary page")
    def proceed_to_summary(self) -> CheckoutSummaryPage:
        self.page.wait_for_load_state('networkidle')
        self.proceed_to_summary_button.click()
        return CheckoutSummaryPage(self.page)
        

