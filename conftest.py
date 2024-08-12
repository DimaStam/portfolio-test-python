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

# @pytest.fixture
# def page(browser, request):
#     page = browser.new_page()
#     failed_before = False
#     try:
#         yield page
#     except Exception as e:
#         # If an exception occurs, take a screenshot before closing the page
#         failed_before = True
#         with allure.step("Taking a screenshot on failure"):
#             screenshot_bytes = page.screenshot(full_page=True)
#             allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)
#         raise  # Re-raise the exception to not mask the test failure
#     finally:
#         # If the test has failed and no exception was raised within the test, take a screenshot here
#         if not failed_before:
#             rep_call = getattr(request.node, "rep_call", None)
#             if rep_call and rep_call.failed:
#                 with allure.step("Taking a screenshot on failure"):
#                     screenshot_bytes = page.screenshot(full_page=True)
#                     allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)
#         page.close()

@pytest.fixture
def page(browser, request):
    page = browser.new_page()
    failed_before = False
    try:
        yield page
    except Exception as e:
        failed_before = True
        take_screenshot(page, request.node.nodeid)
        raise
    finally:
        if not failed_before:
            rep_call = getattr(request.node, "rep_call", None)
            if rep_call and rep_call.failed:
                take_screenshot(page, request.node.nodeid)
        page.close()

def take_screenshot(page, test_name):
    # Replace invalid characters for filenames
    filename = test_name.replace("/", "_").replace(":", "_").replace("[", "_").replace("]", "_") + ".png"
    screenshot_path = f'allure_results/{filename}'
    page.screenshot(path=screenshot_path, full_page=True)
    with allure.step("Taking a screenshot on failure"):
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="screenshot", attachment_type=AttachmentType.PNG)

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
        page.set_viewport_size({"width": 1340, "height": 870})
        # CloseCookies(page).close_cookies()
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
    if report.when == 'call':
        setattr(item, "rep_call", report)

    


    # pytest --alluredir=/Users/global/Desktop/Zegarownia/allure_results
    # allure serve /Users/global/Desktop/Zegarownia/allure_results