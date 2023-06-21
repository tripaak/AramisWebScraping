import scrapy


class BrumbrumSpider(scrapy.Spider):
    name = "brumbrum"
    allowed_domains = ["brumbrum.it"]
    start_urls = ["https://brumbrum.it"]

    def parse(self, response):
        pass
