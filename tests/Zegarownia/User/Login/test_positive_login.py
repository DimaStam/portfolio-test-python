from playwright.sync_api import Page, expect
import pytest
from library.pages.common.HomePage import HomePage
from library.pages.user.LoginPage import LoginPage
from conftest import open_page
from library.testdata.page_titles import PageTitles

@pytest.fixture
def home_page(page: Page, env):
    home_page = HomePage(page)
    open_page(page, env['URL_ZEG'])
    home_page.wait_for_home_page()

    expect(page).to_have_title(PageTitles.ZEG_HOME_PAGE_TITLE)
    return home_page

def test_user_can_login(page, home_page, env):
    login_page: LoginPage = home_page.navigate_to_login_page()
    login_page.wait_for_login_page()

    expect(page).to_have_title(PageTitles.ZEG_LOGIN_TITLE)

    my_account_page = login_page.login_to_system(env['USERNAME_1'], env['PASSWORD'])

    expect(page).to_have_title(PageTitles.ZEG_MY_ACCOUNT_TITLE)

# pytest -v --env=stage tests\Zegarownia\User\Login\test_positive_login.py --headed