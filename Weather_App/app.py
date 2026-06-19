import requests

print("=== WEATHER APP ===")

city = input("Enter city name: ")

# Step 1: Get coordinates from city name
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

geo_response = requests.get(geo_url)

if geo_response.status_code == 200:
    geo_data = geo_response.json()

    if "results" in geo_data:
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2: Get weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"

        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            data = weather_response.json()

            temp = data["current"]["temperature_2m"]
            humidity = data["current"]["relative_humidity_2m"]

            print(f"\n🌤 Weather Report ({city.title()})")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
        else:
            print("Error fetching weather data")
    else:
        print("City not found. Try another name.")
else:
    print("Geocoding failed")
