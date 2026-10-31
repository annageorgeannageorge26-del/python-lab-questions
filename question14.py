import pandas as pd


data = [
    {
        "city": "London",
        "coord": {"lat": 51.51, "lon": -0.13},
        "main": {"temp": 15.5, "humidity": 72}
    },
    {
        "city": "New York",
        "coord": {"lat": 40.71, "lon": -74.01},
        "main": {"temp": 22.0, "humidity": 60}
    },
    {
        "city": "Tokyo",
        "coord": {"lat": 35.68, "lon": 139.65},
        "main": {"temp": 18.2, "humidity": 65}
    }
]


df = pd.json_normalize(data)
df = df.rename(columns={"coord.lat": "lat", "coord.lon": "lon",
                        "main.temp": "temp", "main.humidity": "humidity"})

print(df)

print("\nweather report")
for _, r in df.iterrows():
    print(f"{r.city} ({r.lat}, {r.lon}): {r.temp}°C, humidity {r.humidity}%")