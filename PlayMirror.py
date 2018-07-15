#PlayMirror-MKI
#features: Weather, Clock, News, Calendar, Email
#requirements: Pillow (pip install pillow), Tkinter (pip install tkinter), feedparser (pip install feedparser)
#@author: Gagan Sopori

from tkinter import *
from PIL import Image, ImageTk
import urllib.request, json
import requests
import time
import feedparser


def getLoc():
	try:
		with urllib.request.urlopen("http://ip-api.com/json") as url:
			ip_dat = json.load(url)
		url.close()

		#get the latitude & longitude
		lat = ip_dat['lat']
		lon = ip_dat['lon']
		return lat, lon

	except Exception as e:
		traceback.print_exc()
		return "Error %s: Cannot get location" % e


# Clock Showing Time
# class timeClock:
# 	def clockFormat():


# Weather Updates using OpenWeatherMap API
class weatherUpdate(Frame):
	
	owm_key = 'get yours at openweathermaps.org/api'

	def __init__(self, parent, *args, **kwargs):

		Frame.__init__(self, parent, bg = 'black')

		self.frame = Frame(self, bg = 'black')				#create the frame
		self.frame.pack(side = TOP, anchor = W)				#pack the frame

		
		#icon
		self.iconLabel = Label(self.frame, bg = 'black')				
		self.iconLabel.pack(side = LEFT, anchor = N, padx = 10)

		#temperature
		self.tempLabel = Label(self.frame, font = ('Segoe UI', 72), fg = 'white', bg = 'black')
		self.tempLabel.pack(side = LEFT, anchor = N)

		#maxTemperature
		self.maxLabel = Label(self.frame, font = ('Segoe UI Semilight', 18), fg = 'white', bg = 'black')
		self.maxLabel.pack(side = TOP, anchor = W, padx = 5, pady = 25)

		#minTemperature
		self.minLabel = Label(self.frame, font = ('Segoe UI Semilight', 18), fg = 'white', bg = 'black')
		self.minLabel.pack(side = TOP, anchor = W, padx = 5)

		#location
		self.locLabel = Label(self.frame, font = ('Segoe UI', 12), fg = 'white', bg = 'black')
		self.locLabel.pack(side = TOP, anchor = W, pady = 2)

		#conditionDescription
		self.conditionLabel = Label(self.frame, font = ('Segoe UI Semilight', 24), fg = 'white', bg = 'black')
		self.conditionLabel.pack(side = TOP, anchor = E)

		#forecastTemperature
		self.forecastLabel = Label(self.frame, font = ('Segoe UI', 36), fg = 'white', bg = 'black')
		self.forecastLabel.pack(side = TOP, anchor = W)

		#call the getWeather service
		self.getWeather(lat, lon)
		self.getForecast(lat, lon)


	def getWeather(weather, lat, lon):
		
		weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s' %(lat, lon, weather.owm_key)

		wthr_resp = urllib.request.urlopen(weather_url)
		query = wthr_resp.read().decode('utf-8')			#reading the response
		response_dat = json.loads(query)					#assigning the value into the object
		wthr_resp.close()

		weather.country = response_dat['sys']['country']		#country
		
		location = response_dat['name']							#city
		weather.locLabel.config(text = location)

		desc = response_dat['weather'][0]['main']				#currentCondition
		weather.conditionLabel.config(text = desc)

		if(weather.country == 'US' or weather.country == 'LR' or weather.country == 'MM'):
			
			temperature = ((response_dat['main']['temp'])*(9/5))-459.67			#temperature Farenheit
			weather.tempLabel.config(text = "%.1f"%temperature)

			high = ((response_dat['main']['temp_max'])*(9/5))-459.67
			weather.maxLabel.config(text = "%.1f"%high)

			low = ((response_dat['main']['temp_min'])*(9/5))-459.67
			weather.minLabel.config(text = "%.1f"%low)

		else:
			temperature = response_dat['main']['temp']-273						#temperature Celsius
			weather.tempLabel.config(text = temperature)

			high = response_dat['main']['temp_max']-273
			weather.maxLabel.config(text = high)

			low = response_dat['main']['temp_min']-273
			weather.minLabel.config(text = low)


		iconID = response_dat['weather'][0]['icon']							#iconCode (currentCondition)
		# icon_url = 'http://openweathermap.org/img/w/'+icon+'.png'			#to get Icon(currentCondition)

		#use print statements to check output right now, space to add GUI code

	def getForecast(forecast, lat, lon):
		forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?lat='+str(lat)+'&lon='+str(lon)+'&appid='+forecast.owm_key

		fore_resp = urllib.request.urlopen(forecast_url)
		query2 = fore_resp.read().decode('utf-8')
		resp_2 = json.loads(query2)
		fore_resp.close()
		#print(resp_2)

		if(forecast.country == 'US' or forecast.country == 'LR' or forecast.country == 'MM'):
			
			fore_temp = ((resp_2['list'][0]['main']['temp'])*(9/5))-459.67			#Change the function to get values for all the times
			#print("%.1f"%fore_temp)

		else:

			fore_temp = resp_2['list'][0]['main']['temp']-273						#Change the function to get values for all the times
			#print("%.1f"%fore_temp)


#News Update using feedparser library & News Service
class newsUpdate:

	news_url = 'http://feeds.reuters.com/Reuters/worldNews'

	def getNews(news):

		headline = feedparser.parse(news.news_url)
		length = len(headline)

		for items in headline.entries[0:5]:
			title = headline.entries[len(items)-length].title
			#print(title)
			desc = headline.entries[len(items)-length].description				#check to print the text part
			#print(desc)
			length = length-1




















lat, lon = getLoc()
root=Tk()
topFrame = Frame(root, bg = 'black')
bottomFrame = Frame(root, bg = 'black')
topFrame.pack(side = TOP, fill = BOTH, expand = YES)
bottomFrame.pack(side = BOTTOM, fill = BOTH, expand = YES)

W_Up = weatherUpdate(topFrame)
W_Up.getWeather(lat, lon)
W_Up.pack(side=LEFT, anchor=N, padx=50, pady=50)
# W_Up.getForecast(lat, lon)
# N_Up = newsUpdate()
# N_Up.getNews()
root.mainloop()

