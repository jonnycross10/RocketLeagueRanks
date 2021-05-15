import requests
import json

headers = {
    'authority': 'api.tracker.gg',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'origin': 'https://rocketleague.tracker.network',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://rocketleague.tracker.network/',
    'cookie': 'X-Mapping-Server=s6; __cflb=02DiuFQAkRrzD1P1mdjW28WYn2UPf2uFA6muZXymvW5Ek',
}

params = (
    ('season', '17'),
)

response = requests.get('https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/76561198291004384/segments/playlist', headers=headers, params=params)

r = response.json()

#print(r["data"][0])

for i in r["data"]:
  print(i["metadata"]["name"])
