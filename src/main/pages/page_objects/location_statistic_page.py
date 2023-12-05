from typing import Union

from src.main.browser.browser_manager import BrowserPage
from src.main.config import PROJECT_ABSPATH
from src.main.pages.page_elements.statistic_elements import StatisticElements


class StatisticPage(BrowserPage):

    def __init__(self):
        super().__init__()
        self.statistic_elements = StatisticElements()

    def open_page(self, partner: Union[int, str], location: Union[int, str]) -> 'StatisticPage':
        self.open_url("file://" + PROJECT_ABSPATH + f"/main/resources/P{partner}L{location}.mht")
        return self

    def get_location_title(self) -> str:
        return self.page.locator(self.statistic_elements.location_title).text_content().strip()

    def get_comparing_period(self) -> str:
        return self.page.text_content(self.statistic_elements.comparing_period).strip().removeprefix("vs").strip()

    def get_metric_value(self, metric_name: str) -> str:
        return self.page.locator(self.statistic_elements.metric_component, has_text=metric_name).locator(
            self.statistic_elements.metric_digit).text_content().strip()

    def get_selected_date(self) -> str:
        return self.page.text_content(self.statistic_elements.selected_date).strip()
