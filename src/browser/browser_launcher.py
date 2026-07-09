from playwright.sync_api import sync_playwright

import yaml

class BrowserLauncher:
    #Класс для инициализации браузера
    def __init__(self, local_browser_config_path= None):
        self.config = None
        self._load_config(local_browser_config_path)
        self.context = None
        self.browser = None
        self.playwright = sync_playwright().start()
        self._launch()

    def _load_config(self, config_path):
        #Безопасно считывает конфиг в переменную
        try:
            with open(config_path, "r") as config_p:
                self.config = yaml.safe_load(config_p)
        except Exception as e:
            raise RuntimeError(f"Ошибка во время загрузки конфигурационного файла {e}")

    def _launch(self):
        #Подготавливает локальный браузер с данной в yaml конфигурацией
        browser_type_name = self.config.get("browserType")
        launch_option = self.config.get("launch")

        if browser_type_name == "chromium":
            browser_type = self.playwright.chromium
        elif browser_type_name == "firefox":
            browser_type = self.playwright.firefox
        else:
            raise ValueError(f"Неизвестный тип браузера: {browser_type_name}")
        
        self.browser = browser_type.launch(**launch_option)

    def _create_context(self, **kwargs):
        #Создание обьекта context
        context_params = {"ignore_https_errors": True}

        if self.config.get("context"):
            context_params.update(self.config["context"])
            
        context_params.update(kwargs)
        self.context = self.browser.new_context(**context_params)

        return self.context

    def create_page(self, **kwargs):
        #Создает обьект page
        context = self._create_context(**kwargs)
        return context.new_page()
    
    def close(self):
        #Закрывает браузер и останавливает процессы Playwright
        if self.browser:
            self.browser.close()
            self.playwright.stop()

