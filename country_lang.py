import scrapy

# Before running the code make sure to go to settings.py and verify the USER_AGENT key is set. 
# Make sure that scrapy is installed. 
# To run the code set the directory in the terminal and type: "scrapy crawl country_name -o country_name.csv "
# Above code will save the result in csv file. 

class CountryNameSpider(scrapy.Spider):
    name = "country_lang"
    allowed_domains = ["www.esky.com"]
    start_urls = ["https://www.esky.com/travel-guide/airline-tickets/customs-and-visa-information/official-languages-in-individual-countries"]

    def parse(self, response):
        countries = response.xpath('//tbody/tr')
        for country in countries:
            name = country.xpath('.//td[1]/p/strong/text()').get()
            language = country.xpath('.//td[2]/p/text()').get()

            yield {
                'country': name,
                'language': language
            }
