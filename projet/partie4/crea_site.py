from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Code HTML intégré
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    	<title>Module d'affichage SVG</title>
    </head>
    <body>
    	<h1>Mon module d'affichage SVG</h1>
    	<iframe src="/static/graphique_disque.svg" width="500px" height="500px"></iframe>
     	<iframe src="/static/graphique_memoire.svg" width="500px" height="500px"></iframe>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
