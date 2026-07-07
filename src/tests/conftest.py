import pytest

from src.pages.main_page import MainPage

@pytest.fixture
def main_page(page):
    page.goto("/", timeout=120000)
    return MainPage(page)



    