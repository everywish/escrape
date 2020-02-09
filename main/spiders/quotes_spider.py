import scrapy


class WpSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        src = getattr(self, 'src', None)
        urls = [
            "http://kfem.or.kr/?feed=rss2",
        ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'body' : post.xpath('description//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }
