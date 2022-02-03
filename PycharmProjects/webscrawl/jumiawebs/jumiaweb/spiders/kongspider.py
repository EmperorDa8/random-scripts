import scrapy


class KongspiderSpider(scrapy.Spider):
    name = 'kongspider'
    allowed_domains = ['hotels.ng/hotels-in-akwaibom/uyo']
    start_urls = ['https://hotels.ng/hotels-in-akwaibom/uyo', 'https://hotels.ng/hotels-in-akwaibom/uyo/2']

    def parse(self, response):
        products = response.css("div.col-xs-12.col-sm-8.row.listing-hotels-details-box")
        for product in products:
            items = {
                "name": product.css("h2.listing-hotels-name::text").get(),
                "address": product.css("p.listing-hotels-address.color-dark.hidden-md.hidden-lg::text").get(),
                "price": product.css("p.listing-hotels-prices-discount::text").get().replace(',','')
            }
            yield items
