import scrapy


class JumiaSpider(scrapy.Spider):
    name = "webjumia"
    start_urls = ["https://www.jumia.com.ng/desktop-computers/",
                  "https://www.jumia.com.ng/desktop-computers/?page=2#catalog-listing",
                  "https://www.jumia.com.ng/desktop-computers/?page=3#catalog-listing"
                  ]

    def parse(self, response, **kwargs):
        for product in response.css("article.prd._fb.col.c-prd"):
            try:
                yield {
                    "name": product.css("h3.name::text").get(),
                    "price": product.css("div.prc::text").get(),
                    "link": product.css("a.core").attrib["href"]
                }
            except:
                yield {
                    "name": product.css("h3.name::text").get(),
                    "price": "out of stock",
                    "link": product.css("a.core").attrib["href"]
                }