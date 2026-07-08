import allure
from playwright.sync_api import Page


class Browser:
    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str):
        #Переходит по указанному url
        with allure.step(f"Переходим по URL {url}"):
            return self.page.goto(url, timeout=120000)
        