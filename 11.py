import requests,json
api_key = "c341e3a5ede9998e3438942cb2f27d12"

base_url = "http://api.openweathermap.org/data/2.5/weather?"
cityname = "hyderabad"
complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
response = requests.get(complete_url)
print(response.text)
#x=dict(response.text)
y=response.json()
print(y["main"])
