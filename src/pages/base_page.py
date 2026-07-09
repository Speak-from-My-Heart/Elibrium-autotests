import allure
from playwright.sync_api import Page, expect

from src.browser.browser import Browser
from src.helper.urls import BASE_URL, CORPORATE_CARDS
from src.page_elements.element import Element


class BasePage:
    def __init__(self, page: Page, url=BASE_URL):
        self.page = page
        self.url = url
        self.browser = Browser(page)

        # self.element_head_title = Element(
        #     "//h1[contains(text(),'Business Payments Made Simple')]"
        # )
        self.element_lable = Element(
            page,
            selector="(//a[@aria-label='Elibrium'])[1]",
            allure_name="Логотип Elibrium",
        )
        self.element_busyness_card_pic = Element(
            page, selector="//img[@alt='Elibrium Visa card on sand']",
            allure_name="Изображение карточки на Main странице",
        )

    def open(self):
        with allure.step(f"Открыть страницу по URL: {self.url}"):
            self.browser.go_to_url(self.url)

    def check_url(self):
        assert BASE_URL == self.page.url

    # Проверки перехода по ссылкам

    # @allure.step("Проверить, что на странице отображается тайтл")
    # def check_title(self):
    #     expect(self.page).to_have_title("Business Payments Made Simple | Elibrium")

    # @allure.step("Проверить, что на главной странице отображается заголовок")
    # def element_is_visible(self):
    #     expect(self.element_head_title).to_be_visible()
