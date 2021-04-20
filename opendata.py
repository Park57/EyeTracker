import shutil, os
from tkinter import *


def repucData(list):
	for nom in list:
		fichier = open('data/sauvegarde/'+dossier, 'r')
		for ligne in fichier:
			print(ligne.split(':')[0])

		fichier.close()

def repucProtocoleInfo(nomProtocole):
	liste = []
	fichier = open('data/protocole/'+nomProtocole+'/info', 'r')
	for ligne in fichier:
		ligne = ligne.replace('\n','')
		liste.append(ligne)
	fichier.close()
	return liste

def repucProtocoles():
	return os.listdir('data/protocole/')
	#for dossier in os.listdir('data/protocole/')

def sauvegarderInfo(nomProtocole, adressImage,nomImage,temps):
	#info : nom,
	dossier = 'data/protocole/'+nomProtocole+'/'
	try:
		os.mkdir(dossier)
	except:
		print('dossier deja existant')
		return False
	newAdress =  dossier + nomImage
	shutil.copy(adressImage,newAdress) #deplace des fichier
	fichier = open(dossier+"info", 'w')

	# fichier.write(nomProtocole+"\n")
	# fichier.write(newAdress+"\n")
	# fichier.write(str(temps)+"\n")
	fichier.write("{}\n".format(nomProtocole))
	fichier.write("{}\n".format(newAdress))
	fichier.write("{}\n".format(str(temps)))
	fichier.close()
	a = repucProtocoleInfo(nomProtocole)
	for b in a:
		print(b)
	return True