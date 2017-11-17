# scrapy runspider myspider.py -o cats.json

import scrapy
from tarentula.items import TarentulaItem

# Global var to count number of followed links
nextit = 0

class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    # URL to scrap
    start_urls = [
        'https://www.youtube.com/results?sp=CAJQFA%253D%253D&search_query=funny+cats',
    ]

    def parse(self, response):
        # Usong the global var
        global nextit
        # Get the all the div 'yt-lockup-content' 
        contents = response.css("div.yt-lockup-content")
        # For each, get attributes 'href' and 'title' of the 'a' element in 'h3' element
        # and put it into an item
        for content in contents:
            item = TarentulaItem()
            item['url'] = content.css("h3 a::attr(href)").extract_first()
            item['title'] = content.css("h3 a::attr(title)").extract_first()
            # Avoid ad links
            if item['url'][:6] == '/watch' :
                yield item

        # Get the first div 'branded-page-box.search-pager.spf-link' (next links) 
        nextbox = response.css("div.branded-page-box.search-pager.spf-link")[0]
        # Get the last 'a' element in previous div and extract attribute 'href' of the other 'a' element within
        nextlink = nextbox.css('a')[-1].css('a::attr(href)').extract_first()
        # If link is present ans if we do nat have iterated enough, follow the link with parsing
        if (nextlink is not None) and (nextit < 3) :
            nextit += 1
            yield response.follow(nextlink, callback=self.parse)

