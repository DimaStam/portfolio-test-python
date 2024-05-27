import pytest
import allure
import os
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
from library.Services.CloseCookies import CloseCookies

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright, pytestconfig):
    headless = not pytestconfig.getoption("--headed")
    with allure.step(f"Launching browser {'in headless mode' if headless else 'with UI'}"):
        browser = playwright.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture
def page(browser, request):
    with browser.new_page() as page:
        yield page
    # After the test: teardown code
    if request.node.rep_call and request.node.rep_call.failed:
            # Only take a screenshot if the test has failed
            with allure.step("Taking a screenshot on failure"):
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='session')
def env(request):
    load_dotenv(find_dotenv(f'.env.{request.config.getoption("--env")}'))
    env_variables = dict(os.environ)
    return env_variables

@allure.step("Opening page at {url}")
def open_page(page, url):
    try:
        page.goto(url, timeout=60000)  # Set a timeout of 60 seconds for navigation
        page.set_viewport_size({"width": 2500, "height": 1440})
        CloseCookies(page).close_cookies()  # Close the cookie banner after the page has loaded
    except Exception as e:
        print(f"Failed to navigate to the URL: {e}")
        allure.attach(str(e), name='Navigation error', attachment_type=AttachmentType.TEXT)
        raise

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Set a report attribute for each phase of a call, which can be "setup", "call", or "teardown"
    setattr(item, "rep_" + report.when, report)


    # pytest --alluredir=C:\Users\Dima\Desktop\Testing\Python_Playwright\ZegarowniaProject\allure_results
    # allure serve C:\Users\Dima\Desktop\Testing\Python_Playwright\ZegarowniaProject\allure_results