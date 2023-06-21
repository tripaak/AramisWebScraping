# @author akash.tripathi
# import spider class which scraps
from AramisWebScraping.spiders.clicars import ClicarsSpider 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime


def crawl_clicars():
    settings = get_project_settings()
    settings['FEEDS'] = {
        f"output_folder/{datetime.today().strftime('%d%m%Y')}/clicars_status_{datetime.today().strftime('%H%M%S')}.csv": {
        'format': 'csv',
        'item_export_kwargs': {
           'include_headers_line': True,
        },
    }
    }
    process = CrawlerProcess(settings)
    process.crawl(ClicarsSpider,)
    process.start()

if __name__ == "__main__":
    crawl_clicars()    