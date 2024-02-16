import scrapy
import json


# Before running the code make sure to go to settings.py and verify the USER_AGENT key is set. 
# Make sure that scrapy is installed. 
# To run the code set the directory as twitchdata in the terminal and type: "scrapy crawl get_twitchdata -o twitch.csv "
# Above code will save the result in csv file named twitch.csv  

class StreamedSpider(scrapy.Spider):
    name = "get_twitchdata"
    allowed_domains = ["sullygnome.com"]
    start_urls = ["https://sullygnome.com/games/streamed"]



    def parse(self, response):
        # This takes the language name and key
        languages = response.xpath("//select[@class='TableLanguagePicker']/option")
        for language in languages:
            key = language.xpath(".//@value").get()
            name = language.xpath(".//text()").get()
            
            # Use the language key and name received above with year and month to generate the API link
            year_list = [str(i) for i in range(2016,2024)]  # Data is available from year 2016 to 2024. 
            months_list = ["january", "february", "march","april", "may", 
                        "june","july", "august", "september","october", "november", "december"]
            for y in year_list:
                for m in months_list:
                    link = f"/api/tables/gametables/getgames/{str(y)}{str(m)}/%20/{key}/1/4/desc/0/100"
                    yield response.follow(url=link, callback=self.parse_link, meta={"year":y,"month":m,"language_code":name})
    
    # callback will run the function below which takes all the information. 
    def parse_link(self, response):
        resp = json.loads(response.body)
        data = resp.get('data')
        for row in data:
            name = row.get('name')
            yield {
                "year": response.request.meta['year'],
                "month": response.request.meta['month'],
                "language": response.request.meta['language_code'],
                "id": row.get('id'),
                "name": row.get('name'),
                "watch_time_min": row.get('viewminutes'),
                "stream_time_min": row.get('streamedminutes'),
                "peak_viewers": row.get('maxviewers'),
                "peak_channels": row.get('maxchannels'),
                "streamers": row.get('uniquechannels'),
                "average_viewers": row.get('avgviewers'),
                "average_channels": row.get('avgchannels')
            }

