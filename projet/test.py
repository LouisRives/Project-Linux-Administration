import os
import xml.etree.ElementTree as etree
import datetime
import time

repertoire = "/home/louisrives/documents/projet/sonde"
fichier_xml = "donnees_auto.xml"
duree_validite = 120 # supprimes les vieille donnees toutes les 300 secondes soit 5mins

if os.path.isfile(fichier_xml):
    tree = etree.parse(fichier_xml)
    root = tree.getroot()
else:
    root = etree.Element("datas")
    tree = etree.ElementTree(root)

for fichier in os.listdir(repertoire):
    if fichier.endswith(".txt"):
        with open(os.path.join(repertoire, fichier), "r") as f:
            contenu = f.readlines()
        element = etree.SubElement(root, fichier[:-4])
        for ligne in contenu:
            cle, valeur = ligne.strip().split(":")
            sous_element = etree.SubElement(element, cle.replace(" ","_"))
            sous_element.text = valeur
        element.set("date_creation", time.strftime("%Y-%m-%d %H:%M:%S"))


maintenant = datetime.datetime.now()
enfants_a_supprimer=[]

for child in root.findall(".//*[@date_creation]"):
    date_creation = datetime.datetime.strptime(child.get("date_creation"), "%Y-%m-%d %H:%M:%S")
    diff_temps = maintenant - date_creation
    if diff_temps.total_seconds() > duree_validite:
        enfants_a_supprimer.append(child)
for enfant in enfants_a_supprimer:
    root.remove(enfant)

etree.indent(root)
with open(fichier_xml, 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    tree.write(f,encoding="unicode")

