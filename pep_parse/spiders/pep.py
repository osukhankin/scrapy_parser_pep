import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            'section#numerical-index a[href^="pep-"]'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'title::text'
        ).get().replace(
            '| peps.python.org', ''
        ).split('–', 1)
        yield PepParseItem(
            number=number.replace('PEP', '').strip(),
            name=name.strip(),
            status=response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get().strip()
        )
