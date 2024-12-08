import requests

def connect(status, country):
    link = "https://api.weatherapi.com/v1"
    apiKey = "5af0a3276ab5435f885185215242511"
    country['key'] = apiKey
    url = f"{link}/{status}"
    result = requests.get(url, params=country).json()
    return result

def get_current_temperature(city):
    result = connect(status="current.json", country={"q": city})
    print(result)  # Print the entire response
    if 'current' in result:
        return result['current']['temp_c']
    else:
        print("Error: 'current' key not found or invalid city.")
        return None

def get_temperature_after(city, days, hour=None):
    result = connect(status="forecast.json", country={"q": city, "days": days})
    if 'forecast' in result:
        forecast_day = result['forecast']['forecastday'][days - 1]
        if hour is None:
            return forecast_day['day']['avgtemp_c']
        else:
            return forecast_day['hour'][hour]['temp_c']
    else:
        print("error in finding the city")
        return None

def get_lat_and_long(city):
    result = connect(status="search.json", country={"q": city})
    if result:
        return result[0]['lat'], result[0]['lon']
    else:
        print("error in finding latitude and langitude")
        return None, None

city = "Cairo"
current_temp = get_current_temperature(city)
print(f"the current temperature is : {current_temp}")
temp_after = get_temperature_after(city, days=5)
print(f"temperture after 5 days is : {temp_after}")
lat, lon = get_lat_and_long(city)
print(f" latitude and langitude is : {lat}, {lon}")
