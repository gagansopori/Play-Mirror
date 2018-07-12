# Play-Mirror
Python application that displays weather, headlines, emails, calendar and instagram feed. 

#### MK-I : 
1. Defined Method ***getLoc()***, to get the current location of the user. the methods makes an http request to recieve the coordinates(lat, lon) in json file format. This method shall be used by various classes in the present and the future modules.

2. Defined Class ***weatherUpdate***, contains methods to get current conditions, forecast & historical data for analysis from the [OpenWeatherMap API](https://openweathermap.org/api). This data is analysed using the [NumPy](http://www.numpy.org/) library functions and plotted using [matplotlib](https://matplotlib.org/) functions to show historical trends.
Methods used:
1. *getWeather()*: Calls the weather API to get the current conditions for the given location passing (lat, lon) as arguments every 60 minutes.
2. *getForecast()*: Calls the weather API to get the 3-hour forecasts for the next 5-days passing (lat, lon) as arguments, every 180 minutes.
3. *TBA*: This method will display current conditions, forecast and a graph showing historical data.

#### MK-II : 
1. Defined Class *calenderUpdate*, 



#####TBA
