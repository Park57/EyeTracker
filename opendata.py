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

def sauvegarderInfo(info):
	fichier = open('data/sauvegarde/'+test, 'w')
	shutil.move(info[1],'data/sauvegarde/'+info[0]) #deplace des fichier
	for i in info:
		fichier.write(i+"\n")
	fichier.close()