import requests
import json

API_KEY = 'your_openweathermap_api_key'  # Substitua pela sua chave de API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q='

def get_weather(city):
    try:
        response = requests.get(f"{BASE_URL}{city}&appid={API_KEY}&units=metric")
        data = response.json()

        if data['cod'] == 200:
            print(f"Clima atual em {city}:")
            print(f"Temperatura: {data['main']['temp']}°C")
            print(f"Sensação térmica: {data['main']['feels_like']}°C")
            print(f"Umidade: {data['main']['humidity']}%")
            print(f"Condições: {data['weather'][0]['description']}")
        else:
            print(f"Erro: {data['message']}")
    except Exception as e:
        print(f"Erro ao conectar-se à API: {e}")

if __name__ == '__main__':
    city = input("Digite o nome da cidade: ")
    get_weather(city)