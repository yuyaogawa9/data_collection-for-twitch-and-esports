import scrapy
import json
import pandas as pd
from time import sleep


# Before running the code make sure to go to settings.py and verify the USER_AGENT key is set. 
# Make sure that scrapy is installed. 
# To run the code set the directory in the terminal and type: "scrapy crawl get_names -o game_names.csv "
# Above code will save the result in csv file. 

# Here, we will use the GameID contained in the dataset prize_money.csv to get GameNames. 

df = pd.read_csv('prize_money.csv') # <-You might want to provide the absolute path if it does not work. 
unique_game_ids = pd.unique(df['GameId']).tolist()


class GetNamesSpider(scrapy.Spider):
    name = "get_names"
    allowed_domains = ["api.esportsearnings.com"]
    
    def start_requests(self):
        api_key = "?apikey=YourAPIkey" # <- Put your API key after the equality sign. 
        for i in unique_game_ids:
            sleep(1.2)
            gameid=str(i)
            link = f"http://api.esportsearnings.com/v0/LookupGameById{api_key}&gameid={gameid}&format=json"
            yield scrapy.Request(url=link, callback=self.parse, meta={"gameID": gameid},
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                                        })
            
            

    def parse(self, response):
        resp = json.loads(response.body)
        yield {
            'gameID': response.request.meta['gameID'],
            'GameName': resp.get('GameName')
        }


        
