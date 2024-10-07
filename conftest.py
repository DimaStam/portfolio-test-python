import pytest
import allure
import os
import time
import logging
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
from library.Services.CloseCookies import CloseCookies

screenshots_dir = os.path.join(os.getcwd(), "screenshots")
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

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
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def allure_attach_screenshot(page, test_name):
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{int(time.time() * 1000)}.png")
    page.screenshot(path=screenshot_path, full_page=True)
    with open(screenshot_path, "rb") as image_file:
        allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope='session')
def env(request):
    load_dotenv(find_dotenv(f'.env.{request.config.getoption("--env")}'))
    env_variables = dict(os.environ)
    print(env_variables)
    return env_variables

@allure.step("Opening page at {url}")
def open_page(page, url):
    try:
        page.goto(url, timeout=60000)
        page.set_viewport_size({"width": 1700, "height": 900})
        if os.getenv('--env') == 'prod':
            CloseCookies(page).close_cookies()
    except Exception as e:
        print(f"Failed to navigate to the URL: {e}")
        allure.attach(str(e), name='Navigation error', attachment_type=AttachmentType.TEXT)
        raise

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" or report.failed:
        setattr(item, "rep_call", report)

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page):
    yield
    # Check if the test has failed or if rep_call is not set (which indicates an earlier failure)
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # Make the screenshots directory if not exists
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")
        # Take a screenshot of the current page
        screenshot_path = os.path.join("screenshots", f"{request.node.name}.png")
        page.screenshot(path=screenshot_path, full_page=True)
        # Attach the screenshot to the Allure report
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
    


    # pytest --alluredir=/Users/global/Desktop/Zegarownia/allure-results
    # allure serve /Users/global/Desktop/Zegarownia/allure-results