import scrapy
import json
import pprint
from UserCrawler.items import UsercrawlerItem

class DmozSpider(scrapy.Spider):
    name = "so_user"
    allowed_domains = ["http://stackoverflow.com/"]
    jsonfile=open("./UserCrawler/spiders/userlinks.json").read()
    jsondata = json.loads(jsonfile)
    start_urls = jsondata["userLinks"]

    def parse(self, response):
        user_info=[]

        for sel in response.css("div#main-content"):
            item = UsercrawlerItem()
            item["user_link"]=response.url
            item["user_id"] = response.url.split("/")[-2]
            item["question_num"] = sel.css("div.user-stats > div > div > span::text").extract()[1]
            item["answer_num"] = sel.css("div.user-stats > div > div > span::text").extract()[0]
            item["reach_num"] = sel.css("div.user-stats > div > div > span::text").extract()[2]
            item["top_tags"] = sel.css("a.post-tag::text").extract()
            pprint.pprint(item)
            user_info.append(item)
        return user_info
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)