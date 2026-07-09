from abc import ABC

import allure
from playwright.sync_api import Page, expect


class Base(ABC):
    # Базовый класс элементов
    def __init__(self, page: Page, selector: str = None, value: str = None, allure_name=None):
        self.page = page
        self.value = value
        self.allure_name = allure_name

        if self.selector:
            self._element = self.page.locator(self.value)
        else:
            raise ValueError("Не указан локатор элмента")

    def get_element(self):
        #Возвращает локатор элемента
        return self._element
    
    def click(self):
        #Кликает по элементу
        with allure.step(f"Кликаем по элементу {self.allure_name}"):
            self._element.click()

    def check_visible(self, visible: bool=True):
        #Проверяем видимость элемента
        if visible:
            status_element = "Видимый"
        else:
            status_element = "Невидимый"
        with allure.step(f"Проверим, что элемент {self.allure_name} - {status_element}"):
            expect(self._element).to_be_visible(visible=visible)

    def wait_for(self, state: str=None, timeout_msec: int = None):
        #Ожидает когда элемент станет видимым или кликабельным
        if (state == "attached") or (state == "visible"):
            status_element = "Видимый"
        else:
            status_element = "Невидимый"
        with allure.step (f"Ждем, что элемент {self._element} - {status_element}"):
            expect(self._element).wait_for(state=state,timeout=timeout_msec)

    def is_enabled(self):
        with allure.step(f"Проверим что элемент {self._element} включен"):
            expect(self._element).is_enabled()
