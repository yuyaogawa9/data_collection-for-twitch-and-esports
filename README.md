# scraping-research-data
The code contained here will scrape the data from websites. 

Scrape_file
1) First run the get_twitchdata.py to obtain the twitch data from https://sullygnome.com/games/streamed
2) Run the get_prize.py to obtain the tournament data from esportsearnings.com 
3) Unfortunately above dataset does not contain the name of each games, thus we will have to run get_names.py to obtain the names of each games. We will later merge this with the data obtained in step2 using the GameID as a key.
4) Then, run country_lang.py to obtain the language spoken in each countries. We will use this later when identifying the language in each countries. 
