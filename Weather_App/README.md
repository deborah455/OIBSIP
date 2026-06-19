# Weather App (Python)

## Project Description
A Python application that fetches real-time weather data for any city using public APIs. It converts city names into coordinates and retrieves current weather conditions.

## Features
- Accepts user input for any city
- Converts city name to coordinates using Geocoding API
- Fetches real-time weather data
- Displays temperature and humidity
- Handles invalid city input

## APIs Used
- Open-Meteo Geocoding API
- Open-Meteo Weather API

## How It Works
1. User enters a city name
2. App fetches latitude and longitude
3. Weather API is called using coordinates
4. Weather data is displayed

## How to Run
```bash
python3 app.py
