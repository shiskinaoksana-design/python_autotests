import requests

#Создание покемона

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b63f308c825dc65e962f2b66639a7774'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

BODY_Create_pokemon = {
    "name": "Crazy Cup",
    "photo_id": 1011
}

RESPONSE_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = BODY_Create_pokemon )
print(RESPONSE_create.text)

pokemon_id = RESPONSE_create.json()["id"]
print(pokemon_id)

#Смена имени покемона

BODY_Change_name = {
    "pokemon_id": pokemon_id,
    "name": "Super Crazy Cup",
    "photo_id": 1011
}

RESPONSE_change = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = BODY_Change_name )
print(RESPONSE_change.text)

#Поймать покемона в покебол

BODY_to_pokeball = {
    "pokemon_id": pokemon_id
}

RESPONSE_to_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers=HEADER, json = BODY_to_pokeball )
print(RESPONSE_to_pokeball.text)