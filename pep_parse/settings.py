import os

# Basic project information
BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

# Crawler settings
ROBOTSTXT_OBEY = True

# Use AsyncioSelectorReactor for twisted reactor
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

# Pipeline settings
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

# DateTime format for file naming
FILENAME_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# Directory settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_RESULTS_DIR = 'results'

# Feed export settings
FEEDS = {
    f'{OUTPUT_RESULTS_DIR}/pep_%(time)s.csv': {
        'fields': ['number', 'name', 'status'],
        'format': 'csv',
        'overwrite': True,
    },
}
