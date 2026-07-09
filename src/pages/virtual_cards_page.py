from playwright.sync_api import Page

from src.helper.urls import BASE_URL, VIRTUAL_CARDS
from src.pages.base_page import BasePage


class VirtualCardsPage(BasePage):
    def __init__(self, page: Page, url= BASE_URL + VIRTUAL_CARDS):
        super().__init__(page, url)

    def check_logo_redirects_to_main_page(self):
        self.element_lable.click()
        self.element_busyness_card_pic.wait_for()
        return self.check_url()