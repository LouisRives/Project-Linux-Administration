import urllib.request
import re
import http.client
import requests

adresse = "http://www.cert.ssi.gouv.fr/"

contenu_page = urllib.request.urlopen(adresse)
html = contenu_page.read().decode("utf-8")

trouver_alerte = r'<div class="item cert-alert open".*?<span class="item-date">(.*?)<\/span>.*?<span class="item-title">(.*?)<\/span>'
alertes = re.findall(trouver_alerte, html, re.DOTALL)

for alerte in alertes:
    date = alerte[0]
    title = alerte[1]
    print(f"Date : {date}")
    print(f"Titre : {title}")
    print(f"----------------")


