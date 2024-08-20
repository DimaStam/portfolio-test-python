from playwright.sync_api import Page, expect
import pytest
from library.Services.CloseCookies import CloseCookies
from library.pages.common.HomePage import HomePage
from library.pages.Orders.SearchResultPage import SearchResultPage
from library.pages.common.Header import Header
from library.pages.common.ProductPage import ProductPage

from library.pages.Orders.ExtraoptionsPage import ExtraoptionsPage
from library.pages.Orders.CheckoutCartPage import CheckoutCartPage
from library.pages.Orders.StepLoginFormPage import StepLoginFormPage
from library.pages.Orders.CheckoutShippingPage import CheckoutShippingPage
from library.pages.Orders.CheckoutSummaryPage import CheckoutSummaryPage
from library.testdata.Orders.DeliveryMethods import DeliveryMethods
from library.testdata.Orders.AllPaymentMethods import PaymentMethods
from conftest import open_page
from library.testdata.page_titles import PageTitles

@pytest.fixture
def home_page(page: Page, env):
    pytest.skip()
    home_page = HomePage(page)
    open_page(page, env['URL_HOD_CZ'])
    home_page.wait_for_home_page()

    # expect(page).to_have_title(PageTitles.HOD_CZ_HOME_PAGE_TITLE)
    return home_page

def test_buy_product_by_blik(home_page, page: Page):
    pytest.skip()
    search_result_page: SearchResultPage = Header(home_page.page).find_product(ProductNames.product_name)

    expect(search_result_page.product_tile).to_be_visible()

    product_page: ProductPage = search_result_page.select_product()

    expect(product_page.product_description_area).to_be_visible()

    extraoptions_page: ExtraoptionsPage = product_page.add_product_to_the_cart()

    expect(extraoptions_page.extraoptions_area).to_be_visible()

    checkout_cart_page: CheckoutCartPage =  extraoptions_page.navigate_to_the_checkout_cart()

    expect(checkout_cart_page.checkout_cart_area).to_be_visible()

    step_login_form_page: StepLoginFormPage = checkout_cart_page.navigate_to_the_step_login_form_page()

    step_login_form_page.wait_for_step_login_form_page()

    checkout_shipping_page: CheckoutShippingPage = step_login_form_page.select_buy_as_guest_user() 

    expect(checkout_shipping_page.shipping_form).to_be_visible()

    checkout_shipping_page.fill_shipping_form()
    checkout_shipping_page.select_delivery_method(DeliveryMethods.balikovna)
    checkout_shipping_page.select_balikovna_delivery_point()

    checkout_summary_page: CheckoutSummaryPage = checkout_shipping_page.proceed_to_summary()

    expect(checkout_summary_page.summary_area).to_be_visible()

    checkout_summary_page.select_payment_method(PaymentMethods.bank_transfer)
    checkout_summary_page.add_order_comment()
    checkout_summary_page.select_agreement_checkbox(CheckoutSummaryPage.hodinkovna_cz_agreement_checkbox)
    # checkout_summary_page.place_order()

    # expect(page).to_have_title(PageTitles.PAYU_TITLE)

    # pytest -v --env=prod tests\HodinkovnaCZ\Orders\GuestUser\individual_test\Hodinkovna_cz_individual_test.py --headed