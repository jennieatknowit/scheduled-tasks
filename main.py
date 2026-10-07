import requests
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
api_key = os.environ.get("OWM_API_KEY")

LON = 13.003822
LAT = 55.604980
cnt = 4

weather_parameters = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : api_key,
    "cnt": cnt,
}

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OMW_endpoint, params= weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather_list in weather_data["list"]:
     id_weather = int(weather_list["weather"][0]["id"])
     if id_weather < 700:
        will_rain =  True
if will_rain:
    print("Better bring an umbrella!")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Rainy day!\n\nBetter bring an umbrella!"
        )


