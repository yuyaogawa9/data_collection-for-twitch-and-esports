import scrapy
import json

# Make sure that scrapy is installed. 
# Before running the code make sure to go to settings.py and verify the USER_AGENT key is set. 
# Website only allows accessing API once per second. Go to settings.py and set DOWNLOAD_DELAY=1.0
# To run the code set the directory in the terminal and type: "scrapy crawl get_prize -o prize.csv "
# Above code will save the result in csv file. 

class GetPrizeSpider(scrapy.Spider):
    name = "get_prize"
    allowed_domains = ["api.esportsearnings.com"]

    def start_requests(self):
        api_key = "?apikey=YourAPIkey" # <- Put your API key after the equality sign. 
        for i in range(0, 1000000, 100):

            offset = f'&offset={str(i)}'
            
            link = f"http://api.esportsearnings.com/v0/LookupRecentTournaments{api_key}{offset}&format=json"
            try:
                yield scrapy.Request(url=link, callback=self.parse)
            except:
                break
        
        
    def parse(self, response):
        resp = json.loads(response.body) # returns the list
        for i in resp:
            # iterate the list which contains 100 values. 
            yield {
                'TournamentId': i.get('TournamentId'),
                'GameId': i.get('GameId'),
                'TournamentName': i.get('TournamentName'),
                'StartDate': i.get('StartDate'),
                'EndDate': i.get('EndDate'),
                'Location': i.get('Location'),
                'Teamplay': i.get('Teamplay'),
                'TotalUSDPrize': i.get('TotalUSDPrize')
            }
