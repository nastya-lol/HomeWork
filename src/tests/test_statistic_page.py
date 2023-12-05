import pytest

from src.main.config import PROJECT_ABSPATH
from src.main.helpers.csv_handler import CsvHandler
from src.main.models.statistic_model import StatisticModel

partner_and_locator = []
for x in [1, 2]:
    for y in [1, 2, 3]:
        partner_and_locator.append((x, y))

csv_parser = CsvHandler(PROJECT_ABSPATH + '/metrics_parser.csv')
csv_parser.start_write().write_header()


@pytest.mark.parametrize("partner, location", partner_and_locator)
def test_parse_statistics(open_browser, statistic_page, partner, location):
    statistic_page.open_page(partner, location)
    statistic_model = StatisticModel(partner,
                                     statistic_page.get_location_title(),
                                     statistic_page.get_comparing_period(),
                                     statistic_page.get_metric_value('Money received'),
                                     statistic_page.get_metric_value('Electricity consumed'),
                                     statistic_page.get_selected_date())

    csv_parser.write_rows(statistic_model.to_dict())
