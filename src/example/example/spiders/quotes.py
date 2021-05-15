import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://quotes.toscrape.com", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//span/small[@class='author']/text()").get(),
                'tags': 'tags'
            }
        next_page = response.xpath("//nav/ul[@class='pager']/li[@class='next']/a/@href").get()
        if next_page:
            abs_url = f"https://quotes.toscrape.com{next_page}"
            yield scrapy.Request(
                url = abs_url,
                callback = self.parse
            )
        else:
            print('No Page Left.')
