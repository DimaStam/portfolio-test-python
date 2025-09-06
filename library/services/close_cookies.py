from playwright.sync_api import Page


class CloseCookies:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_button = page.locator("//button[@class='ch2-btn ch2-allow-all-btn ch2-btn-primary']")
        self.main_logo = page.locator("//a[@aria-label='store logo']")

    def close_cookies(self):
        if self.accept_cookies_button.is_visible():
            self.accept_cookies_button.click()
