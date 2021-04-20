from tkinter import *
import cv2
from experimentation import Experimentation
from protocole import Protocole
from gaze_tracking import GazeTracking
from tkinter import filedialog
from tkinter import PhotoImage

#sudo apt-get install python3-pil python3-pil.imagetk
import shutil, os
import PIL
from PIL import ImageTk
from PIL import Image

def repucData(list):
	for nom in list:
		fichier = open('data/sauvegarde/'+dossier, 'r')
		for ligne in fichier:
			print(ligne.split(':')[0])

		fichier.close()

def repucProtocolee(nomProtocole):
	liste = []
	fichier = open('data/protocole/'+nomProtocole+'/info', 'r')
	for ligne in fichier:
		liste.append(ligne)
	fichier.close()
	return liste

def repucProtocole():
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

	fichier.write(nomProtocole+"\n")
	fichier.write(newAdress+"\n")
	fichier.write(str(temps)+"\n")
	fichier.close()
	a = repucProtocolee(nomProtocole)
	for b in a:
		print(b)
	return True