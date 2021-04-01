from tkinter import *
import cv2
from experimentation import Experimentation
from gaze_tracking import GazeTracking
from tkinter import filedialog
from tkinter import PhotoImage


class Protocole:
	def __init__(self,dossier=None):
		if dossier is None:
			#demanderInfo()
			print("yo")
		else :
			self.recupererInfo(dossier)


	def recupererInfo(self,dossier):
		fichier = open('data/sauvegarde/'+dossier, 'r')
		for ligne in fichier:
			print(ligne)

		fichier.close()
