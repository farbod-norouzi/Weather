# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
import platform
from os import system
import sys
import datetime
try:
	from colorama import Fore
except:
   print("Installing prerequisites")
   system("pip install colorama ")
   print("Run Script Again...")

# Enter your API key here
api_key = "41f9fd81f0fbcdf146ba3e0b93250b96"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# Start (Clearing & Banner)

def clear():

	res = platform.uname()[0]
	if res == "Windows":
		system("cls")
	elif res == "Linux":
		system("clear")
clear()

print(Fore.CYAN+"""                                                                          
@@@  @@@  @@@  @@@@@@@@   @@@@@@   @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@   
@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@!  @@!  @@!       @@!  @@@    @@!    @@!  @@@  @@!       @@!  @@@  
!@!  !@!  !@!  !@!       !@!  @!@    !@!    !@!  @!@  !@!       !@!  @!@  
@!!  !!@  @!@  @!!!:!    @!@!@!@!    @!!    @!@!@!@!  @!!!:!    @!@!!@!   
!@!  !!!  !@!  !!!!!:    !!!@!!!!    !!!    !!!@!!!!  !!!!!:    !!@!@!    
!!:  !!:  !!:  !!:       !!:  !!!    !!:    !!:  !!!  !!:       !!: :!!   
:!:  :!:  :!:  :!:       :!:  !:!    :!:    :!:  !:!  :!:       :!:  !:!  
 :::: :: :::    :: ::::  ::   :::     ::    ::   :::   :: ::::  ::   :::  
  :: :  : :    : :: ::    :   : :     :      :   : :  : :: ::    :   : :  
                                                                          """+Fore.RESET)

# End (Banner)

# Give city name
try:
	cnt = input(" Enter Country Name: ")
	city_name = input(" Enter City Name : ")
except:
	print(Fore.RED+"Program Closed!"+Fore.RESET)
	sys.exit()
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values

	celsius = current_temperature - 273.15
	print(Fore.RED+"\n----------------Weather----------------\n"+Fore.RESET)
	# Print Country
	print(Fore.LIGHTMAGENTA_EX+ " Country: "+Fore.RESET+ cnt)
	# Print City
	print(Fore.LIGHTGREEN_EX+ " City: "+Fore.RESET+city_name)
	# Print Date & Time
	datetime_object = datetime.datetime.now()
	print(" Date & Time : \n",datetime_object,'\n')
	# Print Weather Result
	print(Fore.YELLOW+"\n Temperature (in Celsius unit) = " +
					str(round(celsius)) + " °C" + 
		"\n \n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) + " hpa" +
		"\n \n humidity (in percentage) = " +
					str(current_humidity) + "%" +
		"\n \n description = " +
					str(weather_description)+Fore.RESET)
	print(Fore.GREEN+"\n \n Manufacturer : Senior Farbod"+Fore.RESET)

else:
	print(" City Not Found ")

print(Fore.RED+"\n----------------Weather----------------\n"+Fore.RESET)