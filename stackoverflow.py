from scrapy.item import Field
from scrapy.item import Item 
from scrapy.spiders import Spider 
from scrapy.selector import Selector 
from scrapy.loader import ItemLoader 

#1 definir la abstraccion de Clases
class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()
 
#2 definir el Spider
class StackOverflowSpider (Spider):
    name = 'MiPrimerSpider'
    custom_setting = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    
    #3 url semilla
    start_urls = ['https://es.stackoverflow.com/questions']

    #4 llamar a la funcion parse()
    def parse(self, response):
        sel = Selector(response)
        #5 analizar el arbol HTML de la web y aramar la logica para descargar la info
        # el resultado va a ser una lista con varias preguntas       
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')

        i = 0
        for pregunta in preguntas:
            #6 llenar mis items
            item = ItemLoader(Pregunta(), pregunta)
            item.add_value('id', i)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')
            i += 1

            #7 yield de mis items
            yield item.load_item()
    