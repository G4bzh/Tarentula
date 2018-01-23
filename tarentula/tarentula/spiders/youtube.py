# scrapy runspider myspider.py -o cats.json

import scrapy
from scrapy.http.request import Request
from tarentula.items import TarentulaItem


class YoutubeCatsSpider(scrapy.Spider):
    name = "youtube-cats"
    # URL to scrap
    start_urls = [
        'https://www.youtube.com/results?sp=CAJQFA%253D%253D&search_query=funny+cats',
    ]
    iter = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'tarentula.pipelines.SqlitePipeline': 300,
        },
    }

    def parse(self, response):
        # Get the all the div 'yt-lockup-content' 
        contents = response.css("div.yt-lockup-content")
        # For each, get attributes 'href' and 'title' of the 'a' element in 'h3' element
        # and put it into an item
        for content in contents:
            item = TarentulaItem()
            item['url'] = content.css("h3 a::attr(href)").extract_first()
            item['title'] = "ReplaceMe"

            if item['url'][:6] == '/watch' :
                item['url'] = 'https://www.youtube.com' + item['url']
                # Scrap Google image for a thumbnail
                yield Request('https://www.google.fr/search?tbm=isch&q="' + item['title'] + '"'  , callback=self.parseThumbnail,meta={'item': item})

        # Get the first div 'branded-page-box.search-pager.spf-link' (next links) 
        nextbox = response.css("div.branded-page-box.search-pager.spf-link")[0]
        # Get the last 'a' element in previous div and extract attribute 'href' of the other 'a' element within
        nextlink = nextbox.css('a')[-1].css('a::attr(href)').extract_first()
        # If link is present ans if we do nat have iterated enough, follow the link with parsing
        if (nextlink is not None) and (self.iter < 3) :
            self.iter += 1
            yield response.follow(nextlink, callback=self.parse)


    def parseThumbnail(self, response):
        # get item from meta
        item = response.meta['item']
        # Get first image link as item thumb
        item['thumb'] = response.css('table.images_table img::attr(src)').extract_first()
        yield item





class YoutubeCatsTitlesSpider(scrapy.Spider):
    name = "youtube-cats-titles"
    # URL to scrap
    start_urls = [
        'https://www.youtube.com/results?sp=CAJQFA%253D%253D&search_query=funny+cats',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'tarentula.pipelines.SqliteTitlesPipeline': 300,
        },
    }

    def parse(self, response):
        # Get the all the div 'yt-lockup-content' 
        contents = response.css("div.yt-lockup-content")
        # For each, get attributes 'href' and 'title' of the 'a' element in 'h3' element
        # and put it into an item
        for content in contents:
            item = TerrariaItem()
            url = content.css("h3 a::attr(href)").extract_first()
            item['title'] = content.css("h3 a::attr(title)").extract_first()
            try:
                item['title'].encode('ascii')
            except UnicodeEncodeError:
                continue
            else:
                # Avoid ad links
                if 'url'[:6] == '/watch' :
                    yield item

        # Get the first div 'branded-page-box.search-pager.spf-link' (next links) 
        nextbox = response.css("div.branded-page-box.search-pager.spf-link")[0]
        # Get the last 'a' element in previous div and extract attribute 'href' of the other 'a' element within
        nextlink = nextbox.css('a')[-1].css('a::attr(href)').extract_first()
        # If link is present follow the link with parsing
        if nextlink is not None :
            yield response.follow(nextlink, callback=self.parse)