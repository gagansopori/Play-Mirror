#PlayMirror-MKI
#features: Weather, Clock, Instagram, Email, Calendar, News
#requirements: Pillow (pip install pillow), Tkinter(pip install tkinter (not for version 3.3 & above))
#@author: Gagan Sopori

import urllib.request, json
import time
from tkinter import *
from PIL import Image, ImageTk


# class timeClock:
# 	def clockFormat():

def getLoc():
	with urllib.request.urlopen("http://ip-api.com/json") as url:
		ip_dat = json.load(url)
	url.close()

	#get the latitude & longitude
	lat = ip_dat['lat']
	lon = ip_dat['lon']
	return lat, lon

class weatherUpdate:
	
	owm_key = '1ba4271ee4e9387e33e0d4275c045c81'

	def getWeather(weather, lat, lon):
		
		weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&appid='+weather.owm_key

		wthr_resp = urllib.request.urlopen(weather_url)
		query = wthr_resp.read().decode('utf-8')			#reading the response
		response_dat = json.loads(query)					#assigning the value into the object
		wthr_resp.close()

		weather.country = response_dat['sys']['country']		#country
		location = response_dat['name']							#city
		desc = response_dat['weather'][0]['main']				#currentCondition

		if(weather.country == 'US' or weather.country == 'LR' or weather.country == 'MM'):
			temperature = ((response_dat['main']['temp'])*(9/5))-459.67			#temperature Farenheit
			high = ((response_dat['main']['temp_max'])*(9/5))-459.67
			low = ((response_dat['main']['temp_min'])*(9/5))-459.67

		else:
			temperature = response_dat['main']['temp']-273						#temperature Celsius
			high = response_dat['main']['temp_max']-273	
			low = response_dat['main']['temp_min']-273


		icon = response_dat['weather'][0]['icon']			#iconCode (currentCondition)
		icon_url = 'http://openweathermap.org/img/w/'+icon+'.png'			#to get Icon(currentCondition)

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


class getInstagram:

	



















W_Up = weatherUpdate()
lat, lon = getLoc()
W_Up.getWeather(lat, lon)
W_Up.getForecast(lat, lon)
