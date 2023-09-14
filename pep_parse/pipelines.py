import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import RESULTS_DIR, BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def __init__(self, *args, **kwargs):
        (BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_name = (
            f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}'
            f'.csv')
        file_path = BASE_DIR / RESULTS_DIR / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'Количество'),
                *self.results.items(),
                ('Всего', sum(self.results.values()) - 1)
            ])
