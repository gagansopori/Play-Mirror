#PlayMirror-MKI
#features: Weather, Clock, News, Calendar, Email
#requirements: Pillow (pip install pillow), Tkinter (pip install tkinter), feedparser (pip install feedparser), pandas (pip install pandas)
#@author: Gagan Sopori

from tkinter import *
from PIL import Image, ImageTk
from pandas.io.json import json_normalize
import urllib.request, json
import requests
import time
import feedparser
import pandas
import csv


#function to get location using IP address
def getLoc():
	try:
		with urllib.request.urlopen("http://ip-api.com/json") as url:
			ip_dat = json.load(url)
		url.close()

		#get the latitude & longitude
		lat = ip_dat['lat']
		lon = ip_dat['lon']
		city = ip_dat['city']
		state = ip_dat['region']

		return lat, lon, state, city

	except Exception as e:
		traceback.print_exc()
		return "Error %s: Cannot get location" % e


# Clock Showing Time
class timeClock(Frame):

	def __init__(self, parent, *args, **kwargs):

		Frame.__init__(self, parent, bg = 'black')

		self.frame = Frame(self, bg = 'black')				#create the frame
		self.frame.pack(side = TOP, anchor = E)				#pack the frame

		#time
		self.timeLabel = Label(self.frame, font = ('Segoe UI', 60), fg = 'white', bg = 'black')
		self.timeLabel.pack(side = TOP, anchor = NE)

		#location
		self.locLabel = Label(self.frame, font = ('Segoe UI', 22), fg = 'white', bg = 'black')
		self.locLabel.pack(side = TOP, anchor = NE, padx = 10, pady = 10)

		#date
		self.dateLabel = Label(self.frame, font = ('Segoe UI', 22), fg = 'white', bg = 'black')
		self.dateLabel.pack(side = TOP, anchor = NE)


	def getTime(tick, city, state):

		timer = time.strftime('%I:%M %p')
		tick.timeLabel.config(text = timer)
		tick.locLabel.config(text = "%s, %s" %(city, state))


# Weather Updates using OpenWeatherMap API
class weatherUpdate(Frame):
	
	owm_key = 'get your own at owm api'

	def __init__(self, parent, *args, **kwargs):

		Frame.__init__(self, parent, bg = 'black')

		self.frame = Frame(self, bg = 'black')				#create the frame
		self.frame.pack(side = TOP, anchor = W)				#pack the frame

		
		#temperature
		self.tempLabel = Label(self.frame, font = ('Segoe UI', 60), fg = 'white', bg = 'black')
		self.tempLabel.pack(side = TOP, anchor = NW)

		#icon
		self.iconLabel = Label(self.frame, bg = 'green', height = 75, width = 75)			
		self.iconLabel.pack(side = LEFT, anchor = NW, padx = 20)

		#conditionDescription
		self.conditionLabel = Label(self.frame, font = ('Segoe UI', 18), fg = 'white', bg = 'black')
		self.conditionLabel.pack(side = TOP, anchor = NW, padx = 10)

		#max\minTemperature
		self.maxminLabel = Label(self.frame, font = ('Segoe UI', 16), fg = 'white', bg = 'black')
		self.maxminLabel.pack(side = LEFT, anchor = NW, padx = 10, pady = 10)

		#forecastTemperature
		self.forecastLabel = Label(self.frame, font = ('Segoe UI', 14), fg = 'white', bg = 'black')
		self.forecastLabel.pack(side = TOP, anchor = W)

	def getWeather(weather, lat, lon):
		
		weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s' %(lat, lon, weather.owm_key)

		wthr_resp = urllib.request.urlopen(weather_url)
		query = wthr_resp.read().decode('utf-8')			#reading the response
		response_dat = json.loads(query)					#assigning the value into the object
		wthr_resp.close()
		
		weather.country = response_dat['sys']['country']				#country
		location = response_dat['name']									#city

		desc = response_dat['weather'][0]['main']						#currentCondition
		weather.conditionLabel.config(text = desc)
		
		####### Error Region Still Working on it##########################################################################		
		weather.iconID = response_dat['weather'][0]['icon']						#iconCode (currentCondition)
		weather.icon = PhotoImage("/assets/icon/%s.png"%weather.iconID)
		weather.iconLabel.config(image=weather.icon)
		weather.iconLabel.image = weather.icon
		##################################################################################################################
		
		if(weather.country == 'US' or weather.country == 'LR' or weather.country == 'MM'):
			deg = u'\u00b0'
			temperature = ((response_dat['main']['temp'])*(9/5))-459.67			#temperature Farenheit
			weather.tempLabel.config(text = "%.1f%s"%(temperature,deg))

			high = ((response_dat['main']['temp_max'])*(9/5))-459.67
			low = ((response_dat['main']['temp_min'])*(9/5))-459.67
			weather.maxminLabel.config(text = "H: %.1f | L: %.1f" %(high, low))

		else:
			deg = u'\u00b0'
			temperature = response_dat['main']['temp']-273						#temperature Celsius
			weather.tempLabel.config(text = "%.1f%s"%(temperature, deg))

			high = response_dat['main']['temp_max']-273
			low = response_dat['main']['temp_min']-273
			weather.maxminLabel.config(text = "H: %.1f | L: %.1f" %(high, low))

		return weather.country


#News Update using feedparser library & News Service
class newsUpdate(Frame):

	news_url = 'http://feeds.reuters.com/Reuters/worldNews'

	def __init__(self, parent, *args, **kwargs):

		Frame.__init__(self, parent, bg = 'black')
		self.frame = Frame(self, bg = 'black')				#create the frame
		self.frame.pack(side = TOP, anchor = W)				#pack the frame


	def getNews(news):

		headline = feedparser.parse(news.news_url)
		length = len(headline)

		for items in headline.entries[0:5]:
			title = headline.entries[len(items)-length].title
			
			news.newsLabel = Label(news.frame, font = ('Segoe UI Semilight', 14), fg = 'white', bg = 'black')
			news.newsLabel.config(text = title)
			news.newsLabel.pack(side = TOP, anchor = E, padx = 20, pady = 2)

			desc = headline.entries[len(items)-length].description				#check to print the text part
			length = length-1


#Forecast Display and Analysis
class forecastUpdate(Frame):

	owm_key = 'get your pwn at owmapi'

	def __init__(self, parent, *args, **kwargs):

		Frame.__init__(self, parent, bg = 'black')

		self.frame = Frame(self, bg = 'black')				#create the frame
		self.frame.pack(side = TOP, anchor = W)				#pack the frame



	def getForecast(forecast, lat, lon, country):
		forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?lat='+str(lat)+'&lon='+str(lon)+'&appid='+forecast.owm_key

		fore_resp = urllib.request.urlopen(forecast_url)
		query2 = fore_resp.read().decode('utf-8')
		resp_2 = json.loads(query2)
		fore_resp.close()
		#print(resp_2)
		df = json_normalize(resp_2['list'])
		df2 = pandas.DataFrame(df)
		df2.to_csv('forecast.csv')


		if(country == 'US' or country == 'LR' or country == 'MM'):
			
			fore_temp = ((resp_2['list'][1]['main']['temp'])*(9/5))-459.67			#Change the function to get values for all the times
			print("%.1f"%fore_temp)

		else:

			fore_temp = resp_2['list'][0]['main']['temp']-273						#Change the function to get values for all the times
			#print("%.1f"%fore_temp)



root=Tk()
topFrame = Frame(root, bg = 'black')
bottomFrame = Frame(root, bg = 'black')
leftFrame = Frame(root, bg = 'black')
rightFrame = Frame(root, bg = 'black')

topFrame.pack(side = TOP, fill = BOTH, expand = YES)
bottomFrame.pack(side = BOTTOM, fill = BOTH, expand = YES)
leftFrame.pack(side = LEFT, fill = BOTH, expand = YES)
rightFrame.pack(side = RIGHT, fill = BOTH, expand = YES)


lat, lon, state, city = getLoc()

#WEATHER
W_Up = weatherUpdate(topFrame)
#NEWS
N_Up = newsUpdate(bottomFrame)
#TIME
T_Up = timeClock(topFrame)
#FORECAST
F_Up = forecastUpdate(leftFrame)

#METHOD CALLS
country = W_Up.getWeather(lat, lon)
F_Up.getForecast(lat, lon, country)
N_Up.getNews()
T_Up.getTime(city, state)

#PACKING FRAMES
W_Up.pack(side = LEFT, anchor = N, padx = 50, pady = 50)		#Weather
N_Up.pack(side = RIGHT, anchor = S, padx = 50, pady = 50)		#News
T_Up.pack(side = RIGHT, anchor = N, padx = 50, pady = 50)		#Date & Time
F_Up.pack(side = LEFT, anchor = N, padx = 50, pady = 50)		#Forecast

root.mainloop()

