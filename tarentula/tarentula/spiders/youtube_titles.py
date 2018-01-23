# scrapy runspider myspider.py -o cats.json

import scrapy
from scrapy.http.request import Request
from tarentula.items import TerrariaItem


class YoutubeTitlesSpider(scrapy.Spider):
    name = "youtube_titles"
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
        #nextbox = response.css("div.branded-page-box.search-pager.spf-link")[0]
        # Get the last 'a' element in previous div and extract attribute 'href' of the other 'a' element within
        #nextlink = nextbox.css('a')[-1].css('a::attr(href)').extract_first()
        # If link is present follow the link with parsing
        #if nextlink is not None :
            # yield response.follow(nextlink, callback=self.parse)

