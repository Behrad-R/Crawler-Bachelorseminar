import scrapy
import os
import numpy as np
import pandas as pd
from scrapy.linkextractors import LinkExtractor
from numpy.lib.function_base import append


class darknetCrawler(scrapy.Spider):
    name = "darknetCrawler2"

    custom_settings ={
        'DEPTH_LIMIT' : 1,
        'DEPTH_PRIORITY': 1
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
            'http://rvy6qmlqfstv6rlz.onion/',
            'http://62gs2n5ydnyffzfy.onion/tunnels/',
            'http://rhe4faeuhjs4ldc5.onion/',
            'http://62gs2n5ydnyffzfy.onion/tunnels/am_hh.html',
            'http://odahix2ysdtqp4lgak4h2rsnd35dmkdx3ndzjbdhk3jiviqkljfjmnqd.onion/',
            'http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/',
            'http://uescqfrcztbhb6tmhdlbejrjfwgtpckcoiwmwq5bfq5hhkwfioan7qad.onion/',
            'http://62gs2n5ydnyffzfy.onion/tunnels/wh_sh.html',
            'http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/',
            'http://ezdhgsy2aw7zg54z6dqsutrduhl22moami5zv2zt6urr6vub7gs6wfad.onion/node/234899',
            'http://w27irt6ldaydjoacyovepuzlethuoypazhhbot6tljuywy52emetn7qd.onion/',
            'http://m6rqq6kocsyugo2laitup5nn32bwm3lh677chuodjfmggczoafzwfcad.onion/media.defcon.org-css/media-faq.html',
            'http://thehubeebh6z6pqdy4wmxdd6d45gmchjm3xe5sdppadna7m3qtmksmid.onion',
            'http://onions53ehmf4q75.onion/tags/securedrop.html',
            'http://ahgpmkiaqfde4innkotgz5q6bgt4gbxmelqod3tjtmpdt3zvxaxareyd.onion',
            'http://aljazeerafo4sau2.onion',
            'http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/',
            'http://okayd5ljzdv4gzrtiqlhtzjbflymfny2bxc2eacej3tamu2nyka7bxad.onion/',
            'http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/',
            'http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/',
            'http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/',
            'http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion/',
            'http://gd5x24pjoan2pddc2fs6jlmnqbawq562d2qyk6ym4peu5ihzy6gd4jad.onion/',
            'http://qazkxav4zzmt5xwfw6my362jdwhzrcafz7qpd5kugfgx7z7il5lyb6ad.onion/',
            'http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion/',
            'http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/',
            'http://ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion/',
            'http://jhi4v5rjly75ggha26cu2eeyfhwvgbde4w6d75vepwxt2zht5sqfhuqd.onion/',
            'http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/',
            'http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/',
            'http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/',
            'http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/',
            'http://kq4okz5kf4xosbsnvdr45uukjhbm4oameb6k6agjjsydycvflcewl4qd.onion/',
            'http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion/',
            'http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/',
            'http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/',
            'http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/',
            'http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/',
            'http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/',
            'http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/',
            'http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion/',
            'http://danschat356lctri3zavzh6fbxg2a7lo6z3etgkctzzpspewu7zdsaqd.onion',
            'http://wi3dg355dpiy2g5k.onion/',
            'http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/',
            'http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/',
            'http://usmost4cbpesx552s2s4ti3c4nk2xgiu763vhcs3b4uc4ppp3zwnscyd.onion/',
            'http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion/',
            'http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/',
            'http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/',
            'http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/',
            'http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/',
            'http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/',
            'http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/',
            'http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/',
            'http://parckwartvo7fskp.onion/',
            'http://notbumpz34bgbz4yfdigxvd6vzwtxc3zpt5imukgl6bvip2nikdmdaad.onion',
            'http://curaj33verawgaddbsdsrzc5krmopfyqnei66io5ldhqwdiqukt4vcyd.onion',
            'http://poeajpn2roedyqqu.onion',
            'http://tapeucwutvne7l5o.onion',
            'http://suprbaydvdcaynfo4dgdzgxb4zuso7rftlil5yg5kqjefnw4wq4ulcad.onion',
            'http://titanxsu7bfd7vlyyffilprauwngr4acbnz27ulfhyxrqutu7atyptad.onion/',
            'http://s6424n4x4bsmqs27.onion',
            'https://3g2upl4pq6kufc4m.onion',
            'http://njalladnspotetti.onion',
            'http://xmrguide42y34onq.onion',
            'http://expyuzz4wqqyqhjn.onion',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open('/home/harald/Desktop/Crawler-Bachelorseminar/darknetSpider/Links2/' + filename, 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {filename}')
        links = response.xpath("//code/text()").extract()
        if response.xpath("//a/@href").extract() != None:
            for link in response.xpath("//a/@href").extract():
                links.append(link)
        yield { 'URL': response.url}
        print(links)
        for link in links:
            try:
                yield response.follow(link, callback= self.parse)
            except Exception:
                pass