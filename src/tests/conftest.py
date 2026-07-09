from pathlib import Path

import pytest

from src.browser.browser_launcher import BrowserLauncher
from src.pages.base_page import BasePage
from src.pages.virtual_cards_page import VirtualCardsPage

config_yaml_path = Path(__file__).parent.parent / "config_browser.yaml"

@pytest.fixture
def browser(request):
    brw = BrowserLauncher(config_yaml_path)
    new_page = brw.create_page()
    #Создаем отслеживание для каждого page
    brw.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield new_page
    #Сохраняем отслеживание каждого теста в файл с отдельным названием
    brw.context.tracing.stop(path=f"traces/{request.node.name}.zip")
    brw.close()

@pytest.fixture
def main_page(browser):
    return BasePage(browser)

@pytest.fixture
def virtual_cards_page(browser):
    return VirtualCardsPage(browser)



    