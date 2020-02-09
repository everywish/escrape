import scrapy
from scrapy.item import Item


class WpSpider(scrapy.Spider):
    name = "wp"

    def start_requests(self):
        url = getattr(self, 'url', None)
        #print(url)
        yield scrapy.Request(url='http://m.cafe.daum.net/21sotong/_rec', callback=self.parse_list)

    def parse_list(self, response):
        #print(response.body)
        #with open("tmp/aa.html", "w") as f:
            #f.write(response.body.decode('utf-8'))

        for article in response.css('ul.list_cafe > li > a'):
            #print(article)
            link = article.css('a::attr(href)').extract_first()
            #print("bb:", link)
            yield scrapy.Request(url='http://m.cafe.daum.net'+link, callback=self.parse_page)

    def parse_page(self, response):

        #with open(f"tmp/bb_{self.ii}.html", "w") as f:
            #f.write(response.body.decode('utf-8'))

        yield {
            'title': response.css('title::text').get(),
            'body': response.css('div#article').get(),
        }
