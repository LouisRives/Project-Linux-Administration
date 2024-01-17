Module d'affichage SVG

Description:
Ce programme Flask permet d'afficher un fichier SVG dans une interface utilisateur web. Les fichiers SVG doivent être placés dans un dossier static dans le même dossier que le fichier Python. L'interface utilisateur est créée à l'aide de code HTML intégré dans le fichier Python.

Installation:
Pour installer les dépendances requises, utilisez la commande suivante :
pip install -r requirements.txt

Pour lancer le serveur Flask, exécutez le fichier Python app.py :
python crea_site.py
Vous pouvez maintenant accéder à l'interface utilisateur en ouvrant votre navigateur et en naviguant vers http://localhost:5000.

Utilisation:
L'interface utilisateur affiche un titre "Module d'affichage SVG" et 2 fichier SVG. Vous pouvez modifier les fichiers SVG en remplaçant le fichier graphique_disque.svg ou graphique_memoire.svg dans le dossier "static" du projet.

Structure de fichiers:
crea_site.py : Le fichier principal de l'application Flask
static/ : le dossier comprenant les fichiers SVG
static/graphique_disque.svg : Le fichier 1 SVG à afficher
static/graphique_memoire.svg : Le fichier 2 SVG à afficher

Dépendances:
Flask

Auteur:
Ce programme a été créé par Louis RIVES-LEHTINEN, louis.rives-lehtinen@alumni.univ-avignon.fr.
