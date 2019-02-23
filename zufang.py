import scrapy
from..items import ShiyanItem

class SpbennsSpider(scrapy.Spider):
    name = 'shiyan'
    allowed_domains = ['hf.58.com']
    def __init__(self):
        self.page = 1
        self.url='http://hf.58.com/chuzu/0/pn{}'
    def start_requests(self):
        url = self.url.format(self.page)
        #url='https://www.wdzj.com/dangan/search?filter=e1&currentPage=3'
        yield scrapy.Request(url=url,callback=self.parse,meta={'po':self.page}) 


    def parse(self, response):
        i=ShiyanItem()
        title= response.xpath('.//div[@class="des"]/h2/a[1]/text()').extract()
        money=response.xpath('.//div[@class="money"]/b/text()').extract()
        typee=response.xpath('.//p[@class="room"]/text()').extract()
        dizhi= response.xpath('.//p[@class="add"]/a/text()').extract()
        #maijia= response.xpath('.//p[@class="geren"]/span/text()').extract()
        name= response.xpath('.//p[@class="geren"]/text()').extract()#'.//div[@class="des"]/div/span/span/text()'
        for z,n,x,c,b in zip(title,money,typee,dizhi,name):
            i['title']=z
            i['money']=n
            i['typee']=x
            i['dizhi']=c
            i['name']=b
            print(i)
            yield i
            po = response.meta.get('po')
            url = self.url.format(po + 1)
            yield scrapy.Request(url,callback=self.parse, meta={'po': po + 1})
   
