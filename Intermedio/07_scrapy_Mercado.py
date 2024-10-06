from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Articulo (Item):
    Titulo = Field()
    Precio = Field()
    Descripcion = Field()

class Mercado_Libre (CrawlSpider):
    name = "Mercado_Libre"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }
    
    download_delay = 1

    allowed_domains = ['motos.mercadolibre.com.co',]
    start_urls = ['https://motos.mercadolibre.com.co/kawasaki/']

    rules = (
        #paginacion
        Rule(
            LinkExtractor(
                allow=r'/_Desde_'
            ), follow=True
        ),
        #Detalle de los productos
        Rule(
            LinkExtractor(
                allow=r'/MCO-'
            ), follow=True, callback='Parse_Item'
        ),
    )

    def parse_Items(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('Titulo', '//h1/text()')
        item.add_xpath('Descripcion', '//div[@class = "ui-pdp-description__content"]/p/text()')
        item.add_xpath('precio', '//span[@class = "andes-money-amount__fraction"]/text()')

        yield item.load_item()
