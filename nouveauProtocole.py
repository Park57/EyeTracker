
from tkinter import *
from parcourirFichier import *
from opendata import *
a = []
def nouveauProtocole():
	window = Tk()
	width_window = window.winfo_screenwidth()
	height_window  = window.winfo_screenheight()
	window.title("Experimentation")
	window.geometry(str(width_window )+"x"+str(height_window ))
	window.minsize(480, 360)
	label_title = Label(window, text="Experimentation parameters",font=("Arial", 40), bg='#4C4B4B', fg='white')
	window.config(background='#4C4B4B')
	button_photo = Button(window, text="ajouter une photo",command= lambda: (b:=choisirImage(window),aa(b)))
	button_photo.pack()
	button_photo.place(x=width_window *3/4,y=height_window/2 )
	button_video = Button(window, text="ajouter une video")
	button_video.pack()
	button_video.place(x=width_window /4,y=height_window/2 )
	button_annule = Button(window, text="annulé",command= lambda: annule(window))
	button_annule.pack(pady = 30 ,side=BOTTOM)

	button_valider = Button(window, text="valider",command= lambda: valider())
	button_valider.pack(pady = 30 ,side=BOTTOM)
	label_title.pack()

	window.mainloop()
	print('yo')
	#canvas = Canvas(window,width = width_window,height=height_window)
	#canvas.pack(expand=YES, fill=BOTH)
def aa(b):
	global a
	a=b

def annule(window):
	window.destroy()
def valider():
	global a
	sauvegarderInfo(["test",a[0], "bonjour"])

