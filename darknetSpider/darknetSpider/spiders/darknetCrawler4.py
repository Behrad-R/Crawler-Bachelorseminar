import scrapy
import os
import numpy as np
import pandas as pd
from scrapy.linkextractors import LinkExtractor
from numpy.lib.function_base import append


class darknetCrawler(scrapy.Spider):
    name = "darknetCrawler4"

    custom_settings ={
        'DEPTH_LIMIT' : 4,
        'DEPTH_PRIORITY': 1
    }
    start_urls = [
            'http://thedarkwebpugv5m.onion/',
            'http://onions53ehmf4q75.onion/',
            'http://onionlinksv3zit3.onion/',
            'http://wikikijoy3lk2anu.onion/',
            'http://darkfailllnkf4vf.onion/',
            'http://rvy6qmlqfstv6rlz.onion/',
            'http://odahix2ysdtqp4lgak4h2rsnd35dmkdx3ndzjbdhk3jiviqkljfjmnqd.onion/',
            'http://rhe4faeuhjs4ldc5.onion/',
            'http://hiddenwikiwpn2ed.onion/',
            'http://darkfailllnkf4vf.onion',
            'http://62gs2n5ydnyffzfy.onion/tunnels/',
            'http://uescqfrcztbhb6tmhdlbejrjfwgtpckcoiwmwq5bfq5hhkwfioan7qad.onion/',
            'http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/',
            'http://politiepcvh42eav.onion',
            'http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/index.html',
            'http://tapeucwutvne7l5o.onion',
            'http://ncidetf3j26mdtvf.onion',
            'http://suprbayoubiexnmp.onion',
            'http://ezdhgsy2aw7zg54z6dqsutrduhl22moami5zv2zt6urr6vub7gs6wfad.onion/node/234899',
            'http://oq7t5ihk4qew5t5s4zghicigokh2ktt575amirsbnilmyawpme6xmyyd.onion',
            'http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/',
            'http://xkkdux37ngz7buxgcf2q5bpf2xdplgt2jcjs52dyjyzb46afg7fqzgad.onion',
            'http://s6424n4x4bsmqs27.onion',
            'http://endchan5doxvprs5.onion',
            'http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion',
            'http://sudsqwx5tewnmlptiybfbjpfaquhekccxls4blqw3znkhnzcy6bwgoid.onion',
            'http://fncuwbiisyh6ak3i.onion',
            'https://3g2upl4pq6kufc4m.onion',
            'http://jthnx5wyvjvzsxtu.onion',
            'http://njalladnspotetti.onion',
            'http://archivecaslytosk.onion',
            'http://dtmfiovjh42uviqez6qn75igbagtiyo724hy3rdxm77dy2m5tt7lbaqd.onion',
            'http://xcln5hkbriyklr6n.onion/en/',
            'http://xmrguide42y34onq.onion',
            'http://expyuzz4wqqyqhjn.onion',
            'http://agoradeska6jfxpf.onion/nojs/captcha',
            'http://localmonerogt7be.onion/nojs/captcha',
            'http://lpiyu33yusoalp5kh3f4hak2so2sjjvjw5ykyvu2dulzosgvuffq6sad.onion',
            'https://www.nytimes3xbfgragh.onion/',
            'https://calyxinstitute.org/projects/digital-services/xmpp',
            'http://j6uhdvbhz74oefxf.onion',
            'http://nzh3fv6jc6jskki3.onion',
            'https://protonirockerxow.onion',
            'https://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/',
            'http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion',
            'https://www.dwnewsvdyyiamwnp.onion/en/top-stories/s-9097',
            'http://2x4tmsirlqvqmwdz.onion',
            'http://darkoddrkj3gqz7ke7nyjfkh7o72hlvr44uz5zl2xrapna4tribuorqd.onion',
            'http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion',
            'http://tt2mopgckifmberr.onion',
            'http://333f7gpuishjximodvynnoisxujicgwaetzywgkxoxuje5ph3qyqjuid.onion',
            'http://lstkx6p3gzsgfwsqpntlv7tv4tsjzziwp76gvkaxx2mqe3whvlp243id.onion',
            'http://televenkzhxxxe6sw4fntkm4csj6s4csqkuczqhrz6aw7ae3me2tjlyd.onion',
            'http://yxuy5oau7nugw4kpb4lclrqdbixp3wvc4iuiad23ebyp2q3gx7rtrgqd.onion',
            'http://cannahomekql6hhg.onion',
            'http://7yipwxdv5cfdjfpjztiz7sv2jlzzjuepmxy4mtlvuaojejwhg3zhliqd.onion',
            'http://q2f7swt5yvbhciqqbbsidufu2vtkv6ivwy6g5i5ukejjlb2jeghd2had.onion/ddos/',
            'http://cieprrpdgp7moka2ktlwy54ooymtgsre23enrf4dfzssap74zz45f6id.onion',
            'http://monopolyberbucxu.onion',
            'http://auzbdiguv5qtp37xoma3n4xfch62duxtdiu4cfrrwbxgckipd4aktxid.onion',
            'http://nzlbyrcvvqtrkxiu.onion',
            'http://2oywvwmtzdelmiei.onion',
            'http://dnmugu4755642434.onion/search',
            'http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/',
            'http://danschat356lctri3zavzh6fbxg2a7lo6z3etgkctzzpspewu7zdsaqd.onion',
            'http://wi3dg355dpiy2g5k.onion/',
            'http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/',
            'http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion/',
            'http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/',
            'http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/',
            'http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/',
            'http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/',
            'http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/',
            'http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/',
            'http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/',
            'http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/',
            'http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/',
            'http://poeajpn2roedyqqu.onion',
            'http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/',
            'http://tapeucwutvne7l5o.onion',
            'http://njalladnspotetti.onion',
            'http://suprbaydvdcaynfo4dgdzgxb4zuso7rftlil5yg5kqjefnw4wq4ulcad.onion',
            'http://titanxsu7bfd7vlyyffilprauwngr4acbnz27ulfhyxrqutu7atyptad.onion/',
            'http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion/',
            'http://parckwartvo7fskp.onion/',
            'http://xmrguide42y34onq.onion',
            'https://3g2upl4pq6kufc4m.onion',
            'http://expyuzz4wqqyqhjn.onion',
            'http://usmost4cbpesx552s2s4ti3c4nk2xgiu763vhcs3b4uc4ppp3zwnscyd.onion/',
            'http://s6424n4x4bsmqs27.onion',
            'http://curaj33verawgaddbsdsrzc5krmopfyqnei66io5ldhqwdiqukt4vcyd.onion',
            'http://notbumpz34bgbz4yfdigxvd6vzwtxc3zpt5imukgl6bvip2nikdmdaad.onion',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open('/home/harald/Desktop/Crawler-Bachelorseminar/darknetSpider/Links4/' + filename, 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {filename}')
        links = response.xpath("//a/@href").extract()
        if response.xpath("//a[contains(.,'security')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'security')]/@href").extract():
                links.append(response.xpath("//a[contains(.,'security')]/@href").extract())
        if response.xpath("//a[contains(.,'breach')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'breach')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'CVE')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'CVE')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'cyber')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'cyber')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'threat')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'threat')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'hack')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'hack')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'expose')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'expose')]/@href").extract():
                links.append(link)
        if response.xpath("//a[contains(.,'software')]/@href").extract() != []:
            for link in response.xpath("//a[contains(.,'software')]/@href").extract():
                links.append(link)
        print(links)
        yield { 
            'URL': response.url,
            'security': response.xpath("//*[contains(.,'security')]").extract(),
            'breach': response.xpath("//*[contains(.,'breach')]").extract(),
            'CVE': response.xpath("//*[contains(.,'CVE')]").extract(),
            'cyber': response.xpath("//*[contains(.,'cyber')]").extract(),
            'threat': response.xpath("//*[contains(.,'threat')]").extract(),
            'hack': response.xpath("//*[contains(.,'hack')]").extract(),
            'expose': response.xpath("//*[contains(.,'expose')]").extract(),
            'software': response.xpath("//*[contains(.,'software')]").extract(),
        }
        for link in links:
            try:
                yield response.follow(link, callback= self.parse)
                yield response.request(link, callback= self.parse)
            except Exception:
                pass