import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b63f308c825dc65e962f2b66639a7774'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '38777'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    data = response_get.json()['data']
    assert data[0]["trainer_name"] == 'Cezar'