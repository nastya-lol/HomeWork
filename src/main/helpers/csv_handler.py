import csv
from typing import Dict

from src.main.models.statistic_model import field_names as fields


class CsvHandler:
    def __init__(self, file_name: str, field_names: Dict[str, str] = fields):
        self.file_name = file_name
        self.field_names = field_names
        self.write_file = None

    def open_csv(self, **kwargs):
        return open(self.file_name, **kwargs)

    def start_write(self, **kwargs) -> 'CsvHandler':
        self.write_file = self.open_csv(mode='w', **kwargs)
        return self

    def write_header(self) -> 'CsvHandler':
        writer = csv.DictWriter(self.write_file, fieldnames=self.field_names)
        writer.writeheader()
        return self

    def write_rows(self, data: Dict[str, str]) -> 'CsvHandler':
        writer = csv.DictWriter(self.write_file, fieldnames=self.field_names)
        writer.writerow(data)
        return self
