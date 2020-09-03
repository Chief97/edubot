from General.Self_Learn_Doubt_Response.DataLoading import DataLoading
from General.Self_Learn_Doubt_Response.Indexing import Indexing
from General.Self_Learn_Doubt_Response.Preprocess import Preprocess
from General.Self_Learn_Doubt_Response.webScraper.webScraper.spiders.chem_spider import ChemistrySpider
from scrapy.crawler import CrawlerProcess


class DoubtResponseService(object):

    def startScraper(self):
        process = CrawlerProcess(settings={
            "FEEDS": {
                "scrapeddata.csv": {"format": "csv"},
            },
        })
        process.crawl(ChemistrySpider)
        process.start()
        print("process started")

    def collect_data(self):
        data_load = DataLoading()
        data = data_load.load_file()
        preprocess = Preprocess()
        text_preprocessing = preprocess.preprocess_text(data)
        return text_preprocessing

    def process_data(self):
        indexing = Indexing()
        index = indexing.index()


