import scrapy


class PepParseItem(scrapy.Item):
    """
    A Scrapy Item class for parsing and storing information about PEPs.

    Attributes:
        number (scrapy.Field): The PEP number.
        name (scrapy.Field): The PEP title.
        status (scrapy.Field): The status of the PEP from the PEP page.
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
