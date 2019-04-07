'''Показывает температуру и состояние неба в указанном городе'''
import pyowm

city = input('Какой город Вас интересует?: ')

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print('В городе' + city + ' сейчас температура: ' + str(temperature) + ' по Цеотсию.')
print('Также, в указанном городе ' + w.get_detailed_status())
