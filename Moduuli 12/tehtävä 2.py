import requests

api_key = "d75882887ed9c18265033344bd4a4300"

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

try:
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        kuvaus = data["weather"][0]["description"]
        lampotila = data["main"]["temp"]
        print(f"Weather: {kuvaus}")
        print(f"Temperature: {lampotila} Celsius")

except Exception as e:
    print("Yhteysvirhe")