import scrapy
import os
import numpy as np
from scrapy.linkextractors import LinkExtractor
from numpy.lib.function_base import append

linkArray = []
crawledLinks = []
widthCounter = 0
MAXWIDTH = 3

class darknetCrawler(scrapy.Spider):
    name = "darknetCrawler"

    

    def start_requests(self):
        urls = [
            #'https://google.com',
            'http://torigonsn3d63cldhr76mkfdzo3tndnl2tftiek55i2vilscufer6ryd.onion/viewforum.php?f=136'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open('/home/harald/Desktop/Crawler-Bachelorseminar/darknetSpider/Links/' + filename, 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {filename}')
        links = response.xpath("//a/@href").extract()
        print(linkArray)
        for link in links:
            try:
                yield scrapy.Request(link, callback= self.parseChild)
            except Exception:
                pass

    def parseChild(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open('/home/harald/Desktop/Crawler-Bachelorseminar/darknetSpider/Links/' + filename, 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {filename}')
        extractedLinks = response.xpath("//a/@href").extract()
        linkArray = np.concatenate(linkArray, extractedLinks)
        print(linkArray)