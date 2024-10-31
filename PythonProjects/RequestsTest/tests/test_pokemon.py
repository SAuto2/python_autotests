import requests
import pytest
URL='https://api.pokemonbattle.ru/v2'
TOKEN='ad750a91c7f47076a30775bbd6918246'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID='7723'

def test_statuscode():
    response_code=requests.get(url=f'{URL}/trainers',params={'trainer_id':TRAINER_ID})
    assert response_code.status_code==200
def test_name():
    response_name=requests.get(url=f'{URL}/trainers',params={'trainer_id':TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name']=='Alex Alex'