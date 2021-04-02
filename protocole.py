from tkinter import *
import cv2
from experimentation import Experimentation
from gaze_tracking import GazeTracking
from tkinter import filedialog
from tkinter import PhotoImage
from plots import *

class Protocole:
	def __init__(self,dossier=None):
		if dossier is None:
			#demanderInfo()
			#print("yo")
			a = 1
		else :
			self.recupererInfo(dossier)


	def recupererInfo(self,dossier):
		fichier = open('data/sauvegarde/'+dossier, 'r')
		for ligne in fichier:
			#print(ligne.split(':')[0])
			a=1

		fichier.close()
