from playwright.sync_api import Page
from dataclasses import dataclass


@dataclass
class ShippingForm:
    user_email: str
    user_first_name: str
    user_last_name: str
    street_address: str
    house_number: str
    post_code: str
    city: str
    phone_number: str


class ShippingFormData:
    def __init__(self, page: Page):
        self.page = page
