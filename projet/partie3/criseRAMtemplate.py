import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Template

cmd = "free | awk 'NR==2{printf \"%.2f\", $3/$2*100}'"

resultat_cmd = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

ram_usage = float(resultat_cmd.stdout.decode().strip())

# Adresse email de l'expéditeur
exp = "louis.rives-lehtinen@alumni.univ-avignon.fr"
mdp = "ert987LEHT1NEN&"

# Adresse email du destinataire
dest = "louis.rives-lehtinen@alumni.univ-avignon.fr"

# Serveur SMTP utilisé pour envoyer l'email
serveur_smtp = "smtpz.univ-avignon.fr"

# Connexion au serveur SMTP
smtp = smtplib.SMTP_SSL(serveur_smtp, 465)
smtp.login(exp,mdp)

mail = MIMEMultipart()
mail['From'] = exp
mail['To'] = exp
mail['Subject'] = "Crise RAM"

if ram_usage < 80: # <80 pour tester vu la ram sature pas
    with open('template.txt', 'r') as f:
        template_str = f.read()
    template = Template(template_str)
    message = template.render(ram_usage =ram_usage )
    mail.attach(MIMEText(message))
    smtp.sendmail(exp, dest, mail.as_string())

# Fermeture de la connexion SMTP
smtp.quit()