import requests
token = '9167aac6a5862098ffd65e45c326981f'
host = 'https://api.pokemonbattle.me:9104'

create_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
}, headers = {'trainer_token':token, 'Content-Type': 'application/json'})
print(create_pokemon.text)
print(create_pokemon.status_code)

change_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5772",
    "name": "Python",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'trainer_token':token, 'Content-Type': 'application/json'})
print(change_pokemon.text)
print(change_pokemon.status_code)

catch_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5772"
}, headers = {'trainer_token':token, 'Content-Type': 'application/json'})
print(catch_pokemon.text)
print(catch_pokemon.status_code)