
import sqlite3
class ShiyanPipeline(object):
    def open_spider(self,spider):
        self.con =sqlite3.connect('shiyan.sqlite')

        self.cu = self.con.cursor()
    def process_item(self, item, spider):
        print(spider.name, 'pipelines')
        insert_sql = "insert into shiyan(title,money,typee,daizhi,maijia,name) values ('{}','{}','{}','{}','{}','{}')".format(item['title'],item['money'],item['typee'],item['dizhi'] ,'个人',item['name'])
        self.cu.execute(insert_sql)
        self.con.commit()
        return item
    def spider_close(self,spider):
        self.con.close()
