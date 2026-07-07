from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.element_head_title = self.page.locator(
            "//h1[contains(text(),'Business Payments Made Simple')]"
        )

    def check_title(self):
        expect(self.page).to_have_title("Business Payments Made Simple | Elibrium")

    def element_is_visible(self):
        expect(self.element_head_title).to_be_visible()
