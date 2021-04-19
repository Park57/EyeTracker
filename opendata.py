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


def repucProtocole():
	return os.listdir('data/protocole/')
	#for dossier in os.listdir('data/protocole/')

def sauvegarderInfo(info):
	#info : nom,
	dossier = 'data/protocole/'+info[2]+'/'
	try:
		os.mkdir(dossier)
	except:
		print('dossier deja existant')

	fichier = open(dossier+"info", 'w')
	shutil.copy(info[1],dossier+info[3]) #deplace des fichier
	for i in info:
		fichier.write(i+"\n")
	fichier.close()