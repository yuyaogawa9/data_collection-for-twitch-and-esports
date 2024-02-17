# scraping-research-data
The code contained here will scrape the data from websites. 

Scraping data:
 Before we begin, install scrapy and set up the environment. You want to then create a file named scrape. 
1) First, in that file you made above, type "scrapy genspider twitchdata sullygnome.com/games/streamed"
This will create the spider file. Now copy and paste get_twitchdata.py I provided and run the file (further instruction is in the get_twitchdata.py)
2) Go to the scrape file and type in "scrapy genspider get_prize api.esportsearnings.com" in the terminal. 
copy and paste the get_prize.py I provided and run the code. 
3) Unfortunately above dataset does not contain the name of each games, thus we will have to run get_names.py to obtain the names of each games (Run the code exactly the same way as above.) We will later merge this with the data obtained in step2 using the GameID as a key.
4) Then, run country_lang.py to obtain the language spoken in each countries. We will use this later when identifying the language in each countries.

After above step is done, you should have four csv files that are attached here. 

Cleaning the data:
 In the research, we will use four data from above plus broadband data which is accessible https://ourworldindata.org/grapher/broadband-penetration-by-country?tab=table


 

