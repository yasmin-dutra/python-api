def save_history(city):
    with open('history.txt', 'a') as file:
        file.write(f"{city}\n")

if __name__ == '__main__':
    city = input("Digite o nome da cidade: ")
    get_weather(city)
    save_history(city)