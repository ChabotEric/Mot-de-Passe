from donnees import *
from random import choice
	
def adm():
	""" création d'un mot de passe pour
	les besoin administratif. Le mot de passe 
	contiendra dans l'ordre: 3 majuscules,
	4 chiffres et 3 minuscule."""
	
	mot_de_passe = ""
	mot_de_passe += choice(maj)
	mot_de_passe += choice(maj)
	mot_de_passe += choice(maj)
	mot_de_passe += choice(chif)
	mot_de_passe += choice(chif)
	mot_de_passe += choice(chif)
	mot_de_passe += choice(chif)
	mot_de_passe += choice(min)
	mot_de_passe += choice(min)
	mot_de_passe += choice(min)
	return mot_de_passe
	

