
from tkinter import *
from parcourirFichier import *
from opendata import *
a = []
def nouveauProtocole(base):
	window = Tk()
	x = 80
	width_window = window.winfo_screenwidth()
	height_window  = window.winfo_screenheight()
	window.title("Experimentation")
	window.geometry(str(width_window )+"x"+str(height_window ))
	window.minsize(480, 360)
	window.config(background='#4C4B4B')
	button_photo = Button(window, text="ajouter une photo",command= lambda: (b:=choisirImage(window),aa(b)))
	button_photo.pack()
	button_photo.place(x=width_window *2/4 - x,y=height_window * 3/5 )
	# button_video = Button(window, text="ajouter une video")
	# button_video.pack()
	# button_video.place(x=width_window /4,y=height_window/2 )
	button_annule = Button(window, text="annulé",command= lambda: annule(window))
	button_annule.pack(pady = 30 ,side=BOTTOM)

	label_temps = Label(window, text="Temps Experimentation",font=("Arial", 12), bg='#4C4B4B', fg='white')
	label_temps.pack()
	label_temps.place(x=width_window *2/4 - x,y=height_window*2/6 - 30)
	scale_temps = Scale(window, bg='#4C4B4B', orient=HORIZONTAL,from_=3, to=30, resolution=1)
	scale_temps.pack()
	scale_temps.place(x=width_window *2/4 - x,y=height_window*2/6)
	button_valider = Button(window, text="valider",command= lambda: (valider(input_name.get(),base,scale_temps.get()),annule(window)))
	button_valider.pack(pady = 30 ,side=BOTTOM)

	label_title = Label(window, text="Nouveau Protocole parametres",font=("Arial", 40), bg='#4C4B4B', fg='white')
	label_title.pack()

	#vcmd = (master1.register(self.validate),'%d',)
    #dlabel_temps = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)
	input_name = Entry(window)
	input_name.insert(0, "NameProtocole")
	input_name.pack()
	input_name.place(x=width_window /2 - x,y=height_window*2/4 )
	window.mainloop()

	#canvas = Canvas(window,width = width_window,height=height_window)
	#canvas.pack(expand=YES, fill=BOTH)
def aa(b):
	global a
	a=b

def annule(window):
	window.destroy()
def valider(name,base,volume):
	global a

	if sauvegarderInfo(name,a[0],a[2],volume) :
		base.updateList(name)



