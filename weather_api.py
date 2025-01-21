import requests
import json
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

#request the data
r = requests.get(url)

data = r.json()

with open("data/json/data.json", "w") as j:
    json.dump(data, j)


hourly = data["hourly"]

new_data = {
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"],
    "humidity": hourly["relative_humidity_2m"],
    "precipitation": hourly["precipitation"],
    "surface_pressure": hourly["surface_pressure"],
}

#add new_data to data frame
df=pd.DataFrame(new_data)

#convert json file to csv file
df.to_csv("new.csv")

df = pd.read_csv("new.csv")


