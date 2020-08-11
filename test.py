import requests

url = "https://chicken-coop.p.rapidapi.com/games/%7Btitle%7D"

querystring = {"platform":"pc"}

headers = {
    'x-rapidapi-host': "chicken-coop.p.rapidapi.com",
    'x-rapidapi-key': "ccf1deb229msh7f504a4bb515fe7p170fb7jsnac008b4dba51"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)