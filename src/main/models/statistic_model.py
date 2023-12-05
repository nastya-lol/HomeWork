from typing import Dict, Union

field_names = ["partner", "location_title", "comparing_period", "money_received",
               "electricity_consumed", "selected_date"]


class StatisticModel:
    def __init__(self, partner: Union[int, str], location_title: str, comparing_period: str,
                 money_received: str, electricity_consumed: str, selected_date: str):
        self.partner = partner
        self.location_title = location_title
        self.comparing_period = comparing_period
        self.money_received = money_received
        self.electricity_consumed = electricity_consumed
        self.selected_date = selected_date

    def to_dict(self) -> Dict[str, Union[int, str]]:
        return {
            'partner': self.partner,
            'location_title': self.location_title,
            'comparing_period': self.comparing_period,
            'money_received': self.money_received,
            'electricity_consumed': self.electricity_consumed,
            'selected_date': self.selected_date
        }
