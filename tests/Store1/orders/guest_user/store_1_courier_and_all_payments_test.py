import pytest
from playwright.sync_api import Page, expect
from library.pages.common.product_page import ProductPage
from library.pages.orders.extraoptions_page import ExtraoptionsPage
from library.pages.orders.checkout_cart_page import CheckoutCartPage
from library.pages.orders.step_login_form_page import StepLoginFormPage
from library.pages.orders.checkout_shipping_page import CheckoutShippingPage
from library.pages.orders.checkout_summary_page import CheckoutSummaryPage
from library.testdata.orders.delivery_methods import DeliveryMethods
from library.testdata.orders.payment_methods.stores_payment_methods import StoresPaymentMethods
from conftest import open_page


@pytest.fixture
def checkout_summary_page(page: Page, env):

    open_page(page, env['URL_STORE_1_PRODUCT'])
    product_page = ProductPage(page)
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
    checkout_shipping_page.select_delivery_method(DeliveryMethods.courier_dhl)

    checkout_summary_page: CheckoutSummaryPage = checkout_shipping_page.proceed_to_summary()
    expect(checkout_summary_page.summary_area).to_be_visible(timeout=20000)

    return checkout_summary_page


@pytest.mark.parametrize("payment_method_name", StoresPaymentMethods.selectors.keys())
def test_buy_product_with_payment_method(checkout_summary_page: CheckoutSummaryPage, payment_method_name, page: Page):
    payment_methods = StoresPaymentMethods(page)
    payment_methods.select_payment_method(payment_method_name)
    if payment_method_name == StoresPaymentMethods.CARD:
        submit_button_locator = checkout_summary_page.card_submit_button_store_1
        checkout_summary_page.fill_card_fields(submit_button_locator)

    checkout_summary_page.add_order_comment()
    checkout_summary_page.select_agreement_checkbox(CheckoutSummaryPage.zeg_agreement_checkbox)

    checkout_summary_page.place_order()
    expect(page).to_have_title(StoresPaymentMethods.expected_titles[payment_method_name], timeout=20000)
