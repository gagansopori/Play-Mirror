# Play-Mirror
Python application that displays weather, headlines, emails, calendar and instagram feed. 

#### MK-I : 
1. ***getLoc***: Method to get the current location of the user. the methods makes an http request to recieve the coordinates(lat, lon) in json file format. This method shall be used by various classes in the present and the future modules.


2. ***timeUpdate***: Class containing methods to get the current time, date and day of week *(Currently im using the system time using the time class in python, but i will soon replace it with the [ntp time](https://developers.google.com/time/))*.

   1. ***getTime***: Method calling the inbuilt time class to get the system time. This method also displays the current city and state

3. ***weatherUpdate***, Class containing methods to get current conditions, forecast & historical data for analysis from the [OpenWeatherMap API](https://openweathermap.org/api). This data shall be analysed **(MK-II)** using the [NumPy](http://www.numpy.org/) library functions and plotted using [matplotlib](https://matplotlib.org/) functions to show historical trends.

    1. ***getWeather***: Method Calling the weather API to get the current conditions for the given location passing (lat, lon) as arguments every 20 minutes

4. ***newsUpdate***: Class containing methods to get the latest news headlines and a short descirption of the news. The Class uses the  [feedparser](https://pypi.org/project/feedparser/) to parse through the RSS feed *(I have used the [Reuters World News](http://feeds.reuters.com/Reuters/worldNews) feed)* and extract the plain text data which are used as headlines.

   1. ***getNews***: Method calling the RSS feed to get the latest headlines from the world news. It uses the [feedparser](https://pypi.org/project/feedparser/) library to parse through the webpage and extract text from the \<title>& \<summary> tags (in this case) to be used as the News Headlines.
   
   **Initialization of the frame labels is buggy (workin on it).** Initialization of labels follow a recursive pattern (5,5,3,3,4,5)

5. ***forecastUpdate***: Class containing method to get the forecast from the API to display and then store in a database for future prediction.
   
#### MK-II : TBA
