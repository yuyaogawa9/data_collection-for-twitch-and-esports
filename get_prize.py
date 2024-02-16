import scrapy
import json
from time import sleep

# Before running the code make sure to go to settings.py and verify the USER_AGENT key is set. 
# Make sure that scrapy is installed. 
# To run the code set the directory in the terminal and type: "scrapy crawl get_prize -o prize.csv "
# Above code will save the result in csv file. 

class GetPrizeSpider(scrapy.Spider):
    name = "get_prize"
    allowed_domains = ["api.esportsearnings.com"]

    def start_requests(self):
        api_key = "?apikey=YourAPIkey" # <- Put your API key after the equality sign. 
        for i in range(0, 100000, 100):
            sleep(1.2)
            offset = f'&offset={str(i)}'
            link = f"http://api.esportsearnings.com/v0/LookupRecentTournaments{api_key}{offset}&format=json"
            yield scrapy.Request(url=link, callback=self.parse,
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                                        })
        
        
    def parse(self, response):
        resp = json.loads(response.body) # returns the list
        if len(resp)>1:
            for i in range(100):
                # iterate the list which contains 100 values. 
                yield {
                    'TournamentId': resp[i].get('TournamentId'),
                    'GameId': resp[i].get('GameId'),
                    'TournamentName': resp[i].get('TournamentName'),
                    'StartDate': resp[i].get('StartDate'),
                    'EndDate': resp[i].get('EndDate'),
                    'Location': resp[i].get('Location'),
                    'Teamplay': resp[i].get('Teamplay'),
                    'TotalUSDPrize': resp[i].get('TotalUSDPrize')
                }