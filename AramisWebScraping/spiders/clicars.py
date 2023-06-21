import scrapy
import csv


class ClicarsSpider(scrapy.Spider):
    name = 'clicars'
    allowed_domains = ['clicars.com']

    def start_requests(self):
        with open('Clicars.csv', 'r') as input:
            reader = csv.DictReader(input)
            for row in reader:
                yield scrapy.Request(row['URL'], callback=self.parse,meta={'vin':row['vin'],'url':row['URL']})


    def parse(self, response):

        item = {}

        item['vin'] = response.meta['vin']
        item['url'] = response.meta['url']
        try:
           item['model'] = response.css('div.car-card-data.col-xs-12>h1::text').get().strip()
        except:
            item['model'] = 'KO'
        try:
            item['status'] = response.css('div.car-card-slider > div.status-badge span::text').get().strip()
        except:
            if item['model'] == 'KO':
                item['status'] = 'KO'
            else:
                item['status'] = 'Available'

        yield item
