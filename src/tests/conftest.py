import pytest

from src.main.browser.browser_manager import browser_manager
from src.main.pages.page_objects.location_statistic_page import StatisticPage


@pytest.fixture(scope="session")
def open_browser():
    browser_manager.open_browser_page()
    yield
    browser_manager.close_browser()


@pytest.fixture(scope="session")
def statistic_page() -> 'StatisticPage':
    return StatisticPage()
