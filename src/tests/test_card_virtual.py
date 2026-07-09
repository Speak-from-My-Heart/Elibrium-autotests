
class TestVirtualCards:
    def test_logo_redirects_to_main_page(self, virtual_cards_page):
        virtual_cards_page.open()
        virtual_cards_page.check_logo_redirects_to_main_page()

