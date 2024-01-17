import xml.etree.ElementTree as ET
import pygal

tree = ET.parse('donnees_auto.xml')

memoire_total = []
memoire_utilise = []
disque_total = []
disque_utilise = []

for elem in tree.findall('.//verif_memoire'):
    memoire_total.append(elem.find('memoire_total').text)
    memoire_utilise.append(elem.find('memoire_utilise').text)

for elem in tree.findall('.//verif_disque'):
    disque_total.append(elem.find('disque_total').text)
    disque_utilise.append(elem.find('disque_utilise').text)


# créer un graphique pour la mémoire
chart1 = pygal.Line(x_label_rotation=20)
chart1.title = 'Évolution de la mémoire'
chart1.x_labels = [elem.get('date_creation') for elem in tree.findall('.//verif_memoire')]
chart1.add('Mémoire utilisée', [int(x.strip('Mo')) for x in memoire_utilise])
chart1.add('Mémoire libre', [int(x.strip('Mo')) for x in memoire_total])

# créer un graphique pour le disque
chart2 = pygal.Line(x_label_rotation=20)
chart2.title = 'Évolution du disque'
chart2.x_labels = [elem.get('date_creation') for elem in tree.findall('.//verif_disque')]
chart2.add('Espace utilisé', [float(x.strip('Go')) for x in disque_utilise])
chart2.add('Espace libre', [float(x.strip('Go')) for x in disque_total])

chart1.render_to_file('graphique_memoire.svg')
chart2.render_to_file('graphique_disque.svg')
