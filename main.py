#from playsound import playsound 
#playsound('/path/file.mp3') <- odtwarza plik file.mp3

import webbrowser
import requests

pageurl = input("podaj adres strony: ")

date=input("podaj pierwsza date: ")
url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

date=input("podaj druga date: ")
url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

date=input("podaj trzecia date: ")
url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)