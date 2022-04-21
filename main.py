import network
import time
import urequests
from machine import Pin
from neopixel import NeoPixel
from secrets import SSID, PW # secrets.py file contains Wi-Fi details
from random import randint


#NeoPixel Setup
neopin = Pin(8, Pin.OUT)
pixels = 25 
np = NeoPixel(neopin, pixels)

#Weather Icons
sun = [2,6,7,8,10,11,12,13,14,16,17,18,22]
cloudy = [7,11,12,13,15,16,17,18,19]
rain_cloud = [7,11,12,13,15,16,17,18,19]
rain1 = [0,4,5,9,10,12,14,17,22]
rain2 = [2,7,10,12,14,15,19,20,24]
lightning_cloud = [2,6,7,8,10,11,12,13,14,16,18,20,22]
lightning = [3,7,11,12,13,17,21]
snow_ice = [0,2,4,7,10,11,12,13,14,17,20,22,24]
fail = [0,4,6,8,12,16,18,20,24]
fail2 = [2,7,10,11,12,13,14,17,22]

#Wi-Fi Setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PW)
time.sleep(5)
print(wlan.isconnected())
print(wlan.ifconfig())
if wlan.isconnected() == True:
	for i in range(3):
		np.fill((0,16,0))
		np.write()
		time.sleep(0.1)
		np.fill((0,0,0))
		np.write()
		time.sleep(0.1)
else:
	for i in range(3):
		np.fill((16,0,0))
		np.write()
		time.sleep(0.1)
		np.fill((0,0,0))
		np.write()
		time.sleep(0.1)
time.sleep(3)
		
while True:
	#Get the weather data
	r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=Blackpool,UK&appid=--YOUR OPEN WEATHER MAP API KEY HERE--").json()
	weather = r["weather"][0]["main"]
	#Change the weather here to test the conditional tests.
	#weather = "Cats and dogs"
	print(weather)
	if weather == "Clear":
		for value in sun:
			np[value] = (255,265,0)
			np.write()
		time.sleep(10)
		np.fill((0,0,0))
		np.write()
	elif weather == "Clouds":
		for value in cloudy:
			print(value)
			np[value] = (8,8,8)
			np.write()
		time.sleep(10)
		np.fill((0,0,0))
		np.write()
	elif weather == "Rain":
		for i in range(10):
			for value in rain1:
				np[value] = (0,8,8)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
			for value in rain2:
				np[value] = (0,8,8)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
	elif weather == "Thunderstorm":
		for i in range(10):
			for value in lightning_cloud:
				np[value] = (8,8,8)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
			for value in lightning:
				np[value] = (8,8,0)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
	elif weather == "Snow":
		for value in snow_ice:
			np[value] = (0,8,8)
			np.write()
		time.sleep(10)
		np.fill((0,0,0))
		np.write()
	else:
		print("No Weather Data")
		for i in range(10):
			for value in fail:
				np[value] = (128,0,0)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
			for value in fail2:
				np[value] = (128,0,0)
				np.write()
			time.sleep(0.5)
			np.fill((0,0,0))
			np.write()
	time.sleep(10)
			
