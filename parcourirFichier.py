from tkinter import filedialog
from tkinter import PhotoImage
import os


def choisirFichier():
	rep = os.getcwd()
	fic = ""
	repfic = ""
	repfic = filedialog.askopenfilename(title="Ouvrir le fichier:", initialdir=rep,
							initialfile=fic, filetypes = [("All", "*"),("Fichiers Python","*.py;*.pyw")])
	if len(repfic) > 0:
		rep=os.path.dirname(repfic)
		fic=os.path.basename(repfic)
	return repfic, rep, fic

def choisirDossier():
	#return : path, path without directory, name directory
	rep = os.getcwd()
	dossier = ""
	repDossier = filedialog.askdirectory(title="Ouvrir le fichier:", initialdir=rep)
	if len(repDossier) > 0:
		rep=os.path.dirname(repDossier)
		dossier=os.path.basename(repDossier)
	return repDossier, rep, dossier

def choisirImage():
	rep = os.getcwd()
	fic = ""
	repfic = ""
	repfic = filedialog.askopenfilename(title="Ouvrir le fichier:", initialdir=rep,
							initialfile=fic, filetypes = [("Image", "*.jpeg;*.jpg;*.icon;*.png")])
	if len(repfic) > 0:
		rep=os.path.dirname(repfic)
		fic=os.path.basename(repfic)
	return repfic, rep, fic