from flask import jsonify

from General.Self_Learn_Doubt_Response.DataLoading import DataLoading
from General.Self_Learn_Doubt_Response.DoubtRespond import DoubtRespond
from General.Self_Learn_Doubt_Response.Indexing import Indexing
from General.Self_Learn_Doubt_Response.Preprocess import Preprocess
from General.Self_Learn_Doubt_Response.webScraper.webScraper.spiders.chem_spider import ChemistrySpider
from scrapy.crawler import CrawlerProcess


class DoubtResponseService(object):

    word_dictionary = []

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
        print("collect data started")
        data_load = DataLoading()
        data = data_load.load_file()
        preprocess = Preprocess()
        text_preprocessing = preprocess.preprocess_text(data)
        return text_preprocessing

    def process_data(self, plot_data):
        indexing = Indexing()
        self.word_dictionary = indexing.index(plot_data)
        print("Running Process...")
        return jsonify(list(self.word_dictionary))

    def respond(self, input_query):
        doubt_response = DoubtRespond()
        response = doubt_response.classify(input_query, self.word_dictionary)
        return response


