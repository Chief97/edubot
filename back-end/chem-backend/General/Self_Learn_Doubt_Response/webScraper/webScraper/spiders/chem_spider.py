import scrapy



class ChemistrySpider(scrapy.spiders.CrawlSpider):
    name = "chemistry_spider"
    start_urls = [
        'http://localhost:3000/electro-chemistry/electrolysis',
        'http://localhost:3000/electro-chemistry/electro-chemical-cells',
    ]

    def parse(self, response, no_times=None):
        # yield {
        #    'titleText': response.css('title ::text').extract()
        # }

        set_selector = '.set'
        for chem in response.css(set_selector):
            name_selector = 'h1 ::text'
            image_identifier = 'img ::attr(class)'
            image_id_selector = 'img ::attr(alt)'
            definition_selector = '.definition::text'
            activity_selector = '.activity::text'
            note_selector = '.note::text'
            reaction_selector = '.reaction::text'
            word_selector = 'p::text'

            yield {
                'topic': chem.css(name_selector).getall(),
                '': chem.css(image_identifier).getall(),
                'image': chem.css(image_id_selector).getall(),
                'definition': chem.css(definition_selector).getall(),
                'activity': chem.css(activity_selector).getall(),
                'notes': chem.css(note_selector).getall(),
                'reaction': chem.css(reaction_selector).getall(),
                'electro': chem.css(word_selector).re(r'electro\w+'),
                'cells': chem.css(word_selector).re(r'cells'),
            }
