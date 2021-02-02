import scrapy
import os
import numpy as np
import pandas as pd
from scrapy.linkextractors import LinkExtractor
from numpy.lib.function_base import append


class darknetCrawler(scrapy.Spider):
    name = "darknetCrawler"

    custom_settings ={
        'DEPTH_LIMIT' : 2,
        'DEPTH_PRIORITY': 0
    }
    start_urls = [
            'http://darkeyepxw7cuu2cppnjlgqaav6j42gyt43clcn4vjjf7llfyly5cxid.onion/',
            'http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/',
            'http://darkfailllnkf4vf.onion/',
            'http://onions53ehmf4q75.onion/',
            'http://hiddenwikiwpn2ed.onion/',
            'http://onionlinksv3zit3.onion/',
            'http://wikikijoy3lk2anu.onion/',
            'http://thedarkwebpugv5m.onion/',
            'http://thedarkwebpugv5m.onion/',
            'http://rvy6qmlqfstv6rlz.onion/',
            'http://62gs2n5ydnyffzfy.onion/tunnels/',
            'http://rhe4faeuhjs4ldc5.onion/'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open('/home/harald/Desktop/Crawler-Bachelorseminar/darknetSpider/Links1/' + filename, 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {filename}')
        links = response.xpath("//code/text()").extract()
        if response.xpath("//a/@href").extract() != None:
            for link in response.xpath("//a/@href").extract():
                links.append(link)
        yield { 'URL': response.url}
        ##print(links)
        for link in links:
            try:
                yield response.follow(link, callback= self.parse)
            except Exception:
                pass
        