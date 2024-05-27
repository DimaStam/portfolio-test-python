import pytest
from playwright.sync_api import Page, expect
from library.pages.common.HomePage import HomePage
from library.pages.Orders.SearchResultPage import SearchResultPage
from library.pages.common.Header import Header
from library.pages.common.ProductPage import ProductPage
from library.testdata.Orders.ProductNames import ProductNames
from library.pages.Orders.ExtraoptionsPage import ExtraoptionsPage
from library.pages.Orders.CheckoutCartPage import CheckoutCartPage
from library.pages.Orders.StepLoginFormPage import StepLoginFormPage
from library.pages.Orders.CheckoutShippingPage import CheckoutShippingPage
from library.pages.Orders.CheckoutSummaryPage import CheckoutSummaryPage
from library.testdata.Orders.DeliveryMethods import DeliveryMethods
from library.testdata.Orders.PaymentMethods.ZegarowniaPaymentMethods import ZegarowniaPaymentMethods
from conftest import open_page
from library.testdata.page_titles import PageTitles
import time

@pytest.fixture
def home_page(page: Page, env):
    home_page = HomePage(page)
    open_page(page, env['URL_ZEG'])
    home_page.wait_for_home_page()

    expect(page).to_have_title(PageTitles.ZEG_HOME_PAGE_TITLE)
    return home_page

@pytest.fixture
def checkout_summary_page(home_page, page: Page):
    search_result_page: SearchResultPage = Header(home_page.page).find_product(ProductNames.product_name)
    expect(search_result_page.product_tile).to_be_visible(timeout=20000)

    product_page: ProductPage = search_result_page.select_product()
    expect(product_page.product_description_area).to_be_visible(timeout=20000)

    extraoptions_page: ExtraoptionsPage = product_page.add_product_to_the_cart()
    expect(extraoptions_page.extraoptions_area).to_be_visible(timeout=20000)

    checkout_cart_page: CheckoutCartPage = extraoptions_page.navigate_to_the_checkout_cart()
    expect(checkout_cart_page.checkout_cart_area).to_be_visible(timeout=20000)

    step_login_form_page: StepLoginFormPage = checkout_cart_page.navigate_to_the_step_login_form_page()
    step_login_form_page.wait_for_step_login_form_page()

    checkout_shipping_page: CheckoutShippingPage = step_login_form_page.select_buy_as_guest_user()
    expect(checkout_shipping_page.shipping_form).to_be_visible(timeout=20000)

    checkout_shipping_page.fill_shipping_form()
    time.sleep(5)
    checkout_shipping_page.select_delivery_method(DeliveryMethods.dhl_pop)
    checkout_shipping_page.select_dhl_pop_delivery_point()

    checkout_summary_page: CheckoutSummaryPage = checkout_shipping_page.proceed_to_summary()
    expect(checkout_summary_page.summary_area).to_be_visible(timeout=20000)

    return checkout_summary_page

# Use pytest.mark.parametrize to create a test instance for each payment method
@pytest.mark.parametrize("payment_method_name", ZegarowniaPaymentMethods.selectors.keys())
def test_buy_product_with_payment_method(checkout_summary_page: CheckoutSummaryPage, payment_method_name, page: Page):
    payment_methods = ZegarowniaPaymentMethods(page)
    payment_methods.select_payment_method(payment_method_name)
    checkout_summary_page.add_order_comment()
    checkout_summary_page.select_agreement_checkbox(CheckoutSummaryPage.zeg_agreement_checkbox)
    # time.sleep(5)
    # checkout_summary_page.place_order()
    
    # expect(page).to_have_title(ZegarowniaPaymentMethods.expected_titles[payment_method_name])



    # pytest -v --env=prod tests\Zegarownia\Orders\GuestUser\DHLPOP\test_buy_product_by_dhl_pop_and_all_payments.py --headed --alluredir=C:\Users\Dima\Desktop\Testing\Python_Playwright\ZegarowniaProject\allure_results
    # allure serve C:\Users\Dima\Desktop\Testing\Python_Playwright\ZegarowniaProject\allure_results