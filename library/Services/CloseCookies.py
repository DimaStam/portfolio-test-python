from playwright.sync_api import Page, expect
import time

class CloseCookies:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_button = page.locator("//button[@class='ch2-btn ch2-allow-all-btn ch2-btn-primary']")
        self.main_logo = page.locator("//a[@aria-label='store logo']")

    def close_cookies(self):
        self.accept_cookies_button.click()
        # time.sleep(3)
        # if self.accept_cookies_button.is_visible():
        #     try:
        #         self.accept_cookies_button.is_visible(timeout=5000)
        #         self.accept_cookies_button.click()
        #     except:
        #         print("The accept cookies button was not clickable within 3 seconds.")
        # return self