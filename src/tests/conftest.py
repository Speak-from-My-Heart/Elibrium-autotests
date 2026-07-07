import pytest

from src.pages.main_page import MainPage


@pytest.fixture
def main_page(page):
    return MainPage(page)



    