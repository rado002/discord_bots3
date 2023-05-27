import requests
URL = "https://www.dittapotek.no/rad-for-bedre-helse/c/AC00000/"
r = requests.get(URL)
print(r.content)