from pathlib import Path

# SCRAPY DEFAULT SETTINGS
BOT_NAME = 'pep_parse'
SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = SPIDER_MODULES[0]
ROBOTSTXT_OBEY = True

# RESULTS
RESULTS_DIR = 'results'

# DIRs and FILENAMES SETTINGS
BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# SCRAPY CUSTOM SETTINGS
FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    },
}

FEED_EXPORTERS = {
    'csv': 'pep_parse.exporters.CustomCsvItemExporter',
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

# HTTP CACHE
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
