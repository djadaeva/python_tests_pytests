import requests
import pytest
token = '9167aac6a5862098ffd65e45c326981f'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id':1761})
    assert response.status_code == 200

@pytest.mark.parametrize('key , value',[('trainer_name', "Lunas")])

def test_treiner_name(key,value):
    response = requests.get(f'{host}/trainers', params={'trainer_id':1761})
    assert response.json()[key]== value