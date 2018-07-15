# Play-Mirror
Python application that displays weather, headlines, emails, calendar and instagram feed. 

#### MK-I : 
1. ***getLoc***: Method to get the current location of the user. the methods makes an http request to recieve the coordinates(lat, lon) in json file format. This method shall be used by various classes in the present and the future modules.

2. ***weatherUpdate***, Class containing methods to get current conditions, forecast & historical data for analysis from the [OpenWeatherMap API](https://openweathermap.org/api). This data shall be analysed **(MK-II)** using the [NumPy](http://www.numpy.org/) library functions and plotted using [matplotlib](https://matplotlib.org/) functions to show historical trends.

    1. ***getWeather***: Method Calling the weather API to get the current conditions for the given location passing (lat, lon) as arguments every 60 minutes.
    2. ***getForecast***: Method calling the weather API to get the 3-hour forecasts for the next 5-days passing (lat, lon) as arguments, every 180 minutes.
    3. ***\__init__\***: This method displays current conditions, forecast and a graph showing historical data **(MK-II)** graphically.

3. ***newsUpdate***: Class containing methods to get the latest news headlines and a short descirption of the news. The Class uses the  [feedparser](https://pypi.org/project/feedparser/) to parse through the RSS feed *(I have used the [Reuters World News](http://feeds.reuters.com/Reuters/worldNews) feed)* and extract the plain text data which are used as headlines.

   1. ***getNews***: Method calling the RSS feed to get the latest headlines from the world news. It uses the [feedparser](https://pypi.org/project/feedparser/) library to parse through the webpage and extract text from the \<title>& \<summary> tags (in this case) to be used as the News Headlines.
   
   
#### MK-II : TBA
