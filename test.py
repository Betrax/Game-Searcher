import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games"

headers = {"x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "ccf1deb229msh7f504a4bb515fe7p170fb7jsnac008b4dba51"}

response = requests.request("GET", url, headers=headers).text

print(response)
