import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (PEP_ALLOWED_DOMAINS, PEP_SPIDER_NAME,
                                PEP_START_URLS)


class PepSpider(scrapy.Spider):
    """Spider for parsing PEP data from peps.python.org."""

    name = PEP_SPIDER_NAME
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

    def parse(self, response):
        """
        Parse the PEP index page and follow links to individual PEPs.

        Args:
            response (scrapy.http.Response):
                The response object containing the HTML of the PEP index page.

        Yields:
            scrapy.Request: Requests to follow links to individual PEP pages.
        """
        for pep_link in response.css(
            'section#numerical-index a[href^="pep-"]'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Parse an individual PEP page and extract data.

        Args:
            response (scrapy.http.Response):
                The response object containing the HTML of an individual page.

        Yields:
            PepParseItem: The item containing the extracted PEP data.

        Extracts:
            - name: The title of the PEP.
            - number: The PEP number.
            - status: The current status of the PEP.

        Logs an error if parsing fails.
        """
        name = response.css("section#pep-content h1::text").get()
        try:
            number = name.split()[1]
            status = response.css("section#pep-content abbr::text").get()
            yield PepParseItem(name=name, number=number, status=status)
        except (AttributeError, TypeError, IndexError) as e:
            self.logger.error(f"Error parsing PEP page: {e}")
