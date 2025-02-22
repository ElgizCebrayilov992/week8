import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # Extracting data from each quote
        for quote in response.css('div.quote'):
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'author_link': quote.css('span a[href*="author"]::attr(href)').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
        
        # Following pagination link if exists
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
# Comment atdim