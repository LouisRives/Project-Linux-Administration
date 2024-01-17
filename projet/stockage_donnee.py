import xml.etree.cElementTree as etree
import os

disqueD = open("sonde/verif_disque.txt",'r')
memoireD = open("sonde/verif_memoire.txt",'r')
nb_connectD = open("sonde/verif_nb_connect.txt",'r')
contenu_disque = disqueD.readlines()
tailleD = []
for line in contenu_disque:
    tmp = line.split(":")
    tailleD.append(tmp[1])

contenu_memoire = memoireD.readlines()
tailleM = []
for line in contenu_memoire:
    tmp = line.split(":")
    tailleM.append(tmp[1])

contenu_nb_connect = nb_connectD.readlines()
tailleNB= []
for line in contenu_nb_connect:
    tmp = line.split(":")
    tailleNB.append(tmp[1])

datas = etree.Element("datas")
disque = etree.SubElement(datas, "disque")
espacetotal = etree.SubElement(disque, "espacetotal")
espacetotal.text = tailleD[0]
espaceutilise = etree.SubElement(disque, "espaceutilise")
espaceutilise.text = tailleD[1]
espacelibre = etree.SubElement(disque, "espacelibre")
espacelibre.text = tailleD[2]

memoire = etree.SubElement(datas, "memoire")
memoire_total = etree.SubElement(memoire, "memoire_total")
memoire_total.text = tailleM[0]
memoire_utilise = etree.SubElement(memoire, "memoire_utilise")
memoire_utilise.text = tailleM[1]
memoire_libre = etree.SubElement(memoire, "memoire_libre")
memoire_libre.text = tailleM[2]

nb_connectes = etree.SubElement(datas, "nb_connect")
nb_connectesF = etree.SubElement(nb_connectes, "nb_connectF")
nb_connectesF.text = tailleNB[0]

etree.indent(datas)

root=etree.Element('datas')
tree=etree.ElementTree(datas)
tree.write('sonde/donnees.xml')
