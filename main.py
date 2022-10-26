
import requests
import json


url = 'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/''Juliantpb?api_key='
current_api = 'RGAPI-b0cbc0a4-3cec-4905-8c79-21c66db40d02'
# how to hide one line from git?



response = requests.get(url + current_api)
print('Response code: ',response)

json_response = response.json()

print(json.dumps(json_response,indent=2))
















# https://developer.riotgames.com/ - link to generate API
# RGAPI-b0cbc0a4-3cec-4905-8c79-21c66db40d02  API KEY