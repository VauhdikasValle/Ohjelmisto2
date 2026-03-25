# import json
# import request
#
# sarja = input("Anna sarja minkä tiedot haluat: ")
#
# pyynto = "https://api.tvmaze.com/search/shows?q" + sarja
# vastaus = request.get(pyynto).json()
# print(json.dumps(vastaus, indent=2))


import requests
import json

hakusana = input("Anna hakusana: ")
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()
print(json.dumps(vastaus, indent=2))