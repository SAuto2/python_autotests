import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN='ad750a91c7f47076a30775bbd6918246'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID='7723'

Body_create={
    "name": "generate",
    "photo_id": -1
}
Body_rename={
    "pokemon_id": "120160",
    "name": "generate",
    "photo_id": -1
}
Body_catch={
    "pokemon_id": "120160"
}
response_create=requests.post(url=f'{URL}/pokemons',headers=HEADER,json=Body_create)
print(response_create.json())
response_rename=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=Body_rename)
print(response_rename.json())
response_catch=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=Body_catch)
print(response_catch.json())
response_trainers=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID},headers=HEADER)
print(response_trainers)
message=response_trainers.json()['data']
print(message)