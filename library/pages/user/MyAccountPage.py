from playwright.sync_api import Page

class MyAccountPage:
    def __init__(self, page: Page):
        self.page = page