from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):
    HEADER_MAP = {
        'name': 'Название',
        'number': 'Номер',
        'status': 'Статус'
    }

    def _write_headers_and_set_fields_to_export(self, item):
        if not self.include_headers_line:
            return
        if not self.fields_to_export:
            if isinstance(item, dict):
                self.fields_to_export = list(item.keys())
            else:
                self.fields_to_export = list(item.fields.keys())
        headers = list(self._build_row(self.fields_to_export))
        headers = [self.HEADER_MAP.get(header, header) for header in headers]
        self.csv_writer.writerow(headers)
