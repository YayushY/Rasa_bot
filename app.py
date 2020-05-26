import requests

def weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=9edf5aaa12b89912f7f1cef77cfa67f9"
    json_weather = requests.get(url).json()
    temp_data = json_weather["main"]
    cur_temp = round(temp_data["temp"]-273,1)
    feels = round(temp_data["feels_like"]-273,1)
    return cur_temp, feels