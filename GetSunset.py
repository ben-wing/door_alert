import requests
import time

r = requests.get('https://api.sunrise-sunset.org/json?lat=42.2808&lng=-83.7430&date=today&formatted=0')

js=r.json()

#print(js['results'])
#print('--------------------------')

sunset_date=js['results'].get('sunset')
#print(sunset_date)
(sunset,junk)=sunset_date.split('+')
print(sunset+'+0000')


