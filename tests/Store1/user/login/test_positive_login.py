from playwright.sync_api import Page, expect
import pytest
from library.pages.common.home_page import HomePage
from library.pages.user.login_page import LoginPage
from conftest import open_page
from library.testdata.page_titles import PageTitles


@pytest.fixture
def home_page(page: Page, env):
    home_page = HomePage(page)
    open_page(page, env['URL_STORE_1'])
    home_page.wait_for_home_page()
    return home_page


def test_user_can_login(page, home_page: HomePage, env: dict):
    login_page: LoginPage = home_page.navigate_to_login_page()
    login_page.wait_for_login_page()
    login_page.login_to_system(env['STORE_1_USERNAME'], env['STORE_1_PASSWORD'])
    expect(page).to_have_title(PageTitles.STORE_1_MY_ACCOUNT_TITLE)
