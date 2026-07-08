import allure
from playwright.sync_api import Page, expect

from src.browser.browser import Browser
from src.helper.urls import BASE_URL


class BasePage:
    def __init__(self, page: Page, url= BASE_URL):
        self.page = page
        self.url = url
        self.browser = Browser(page)
        self.element_head_title = self.page.locator(
            "//h1[contains(text(),'Business Payments Made Simple')]"
        )

    def open(self):
        with allure.step("Открыть страницу по URL"):
            self.browser.go_to_url(self.url)

    @allure.step("Проверить, что на странице отображается тайтл")
    def check_title(self):
        expect(self.page).to_have_title("Business Payments Made Simple | Elibrium")

    @allure.step("Проверить, что на главной странице отображается заголовок")
    def element_is_visible(self):
        expect(self.element_head_title).to_be_visible()
