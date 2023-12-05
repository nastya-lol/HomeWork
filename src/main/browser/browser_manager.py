from playwright.sync_api import sync_playwright, Page


class BrowserManager:
    def __init__(self):
        self.browser = None
        self._page = None

    def open_browser_page(self) -> 'Page':
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self._page = self.browser.new_context().new_page()
        self._page.set_viewport_size({"width": 1920, "height": 1080})
        return self._page

    @property
    def page(self) -> 'Page':
        return self._page

    def close_browser(self) -> 'BrowserManager':
        return self.browser.close()


browser_manager = BrowserManager()


class BrowserPage:

    @property
    def page(self) -> 'Page':
        return browser_manager.page

    def open_url(self, url: str) -> 'BrowserPage':
        self.page.goto(url)
        self.page.wait_for_load_state()
        return self
