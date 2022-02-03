import scrapy
from jumiaweb.jumiaweb.items import JumiaSpiderItem


class JumiaSpider(scrapy.Spider):
    name = "webjumia"
    start_urls = ["https://www.jumia.com.ng/desktop-computers/",
                  "https://www.jumia.com.ng/desktop-computers/?page=2#catalog-listing",
                  "https://www.jumia.com.ng/desktop-computers/?page=3#catalog-listing"
                  ]

    def parse(self, response, **kwargs):
        item= JumiaSpiderItem
        for product in response.css("article.prd._fb.col.c-prd"):
            item["name"]=product.css("h3.name::text").get()
            item["price"]= product.css("div.prc::text").get().replace("N","")
            item["link"]=product.css("a.core").attrib["href"]

        yield item
