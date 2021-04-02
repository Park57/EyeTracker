from tkinter import *
import cv2
from experimentation import Experimentation
from protocole import Protocole
from gaze_tracking import GazeTracking
from tkinter import filedialog
from tkinter import PhotoImage

#sudo apt-get install python3-pil python3-pil.imagetk
import os
import PIL
from PIL import ImageTk
from PIL import Image

# pip install pillow

# creation fenêtre


class Application :

	def __init__(self):
		self.rep=os.getcwd()
		self.fic = ""
		self.repfic = ""
		#im = self.repertoiredetravail()
		print(self.repfic)
		self.window = Tk()
		#self.im = Tk()

		self.x = self.window.winfo_screenwidth()
		self.y = self.window.winfo_screenheight()
		# personnalisation de la fenêtre

		self.window.title("My application")
		self.window.geometry(str(self.x)+"x"+str(self.y))
		self.window.minsize(600, 400)

		#self.window.call('wm', 'iconphoto',self.window._w,PhotoImage(file=self.repfic))
		#self.window.iconbitmap(self.repfic)
		#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/path/to/ico/icon.png')
		#self.window.iconphoto(False, PhotoImage(file=self.repfic))

		self.window.config(background='#4C4B4B')

		self.label_title = Label()
		self.input_name = Entry()
		self.input_surname = Entry()

		self.button_upload = Button()
		self.button_synthesis = Button()
		self.button_start = Button()

		self.label_data = Label()
		self.label_image = Label()
		self.label_sec = Label()
		self.label_speech = Label()

		self.data_check = Checkbutton()
		self.graph_check = Checkbutton()

		self.scale_data = Scale()
		self.scale_volume = Scale()

		self.list = Listbox()

		#variable = StringVar(self.window)
		self.create_widgets()

	def create_widgets(self):

		self.create_title()
		self.create_buttons()
		self.create_labels()
		self.create_checkboxs()
		self.create_scales()
		self.create_multiple()

		self.updatePos()

	def create_title(self):

		# ajout du titre
		self.label_title = Label(self.window, text="Experimentation parameters",
							font=("Arial", 40), bg='#4C4B4B', fg='white')
		self.label_title.pack()
		self.label_title.place(height=self.y /4, width=self.x )

	def create_buttons(self):

		# ajout champ de saisie
		self.input_name = Entry(self.window)
		self.input_name.insert(0, "Name")
		#self.input_name.place(x= self.x / 5, y =  self.y / 4)

		self.input_surname = Entry(self.window)
		self.input_surname.insert(0, "Surname")
		self.input_surname.pack()
		#self.input_surname.place(x=self.x *3/5, y= self.y /4)

		self.button_upload = Button(self.window, text="Upload new image/ ?cree une nouvelle experimentation ?",command=self.upload)
		self.button_upload.pack()
		#self.button_upload.place(x= self.x/5	,  y= self.y * 4/6)

		self.button_synthesis = Button(self.window, text="Speech Synthesis question")
		self.button_synthesis.pack()
		#self.button_synthesis.place(x=self.x * 3/5, y=self.y * 4/6)

		self.button_start = Button(self.window, text="Start experimation",command=start_experimentation)
		#self.button_start.pack(pady = 30 ,side=BOTTOM)


	def create_labels(self):

		# ajout checkbox
		self.label_data = Label(self.window, text="Save data", font=(
			"Arial", 12), bg='#4C4B4B', fg='white')
		#self.label_data.place(x=self.x/5 +35, y=self.y*2/6 )



		self.label_image = Label(self.window, text="Save graph image",
						   font=("Arial", 12), bg='#4C4B4B', fg='white')
		#self.label_image.place(x=self.x/5 +35, y=self.y*3/7)


		self.label_sec = Label(self.window, text="Data per second",
				   font=("Arial", 12), bg='#4C4B4B', fg='white')
		self.label_sec.pack()
		#self.label_sec.place(x=self.x/5, y=self.y*4/8)

		self.label_speech = Label(self.window, text="Volume speech synthesis",
					 font=("Arial", 12), bg='#4C4B4B', fg='white')
		self.label_speech.pack()
		#self.label_speech.place(x=self.x* 3/5, y=self.y*4/8)




	def create_checkboxs(self):

		self.data_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		self.data_check.select()
		self.data_check.pack()
		#self.data_check.place(x=self.x/5, y=self.y*2/6)

		self.graph_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		self.graph_check.select()
		self.graph_check.pack()
		#self.graph_check.place(x=self.x/5, y=self.y*3/7)
	def create_multiple(self):

		x = ["Eperiance Photo", "Video Homme", "Video Femme", "Photo Visage", "Photo objet"]
		self.list = Listbox(self.window, selectmode = "multiple",bg="green",selectbackground = "red",height=len(x) )
		self.list.pack()

		for each_item in range(len(x)):
			self.list.insert(END, x[each_item])
			self.list.activate(each_item)

	def create_scales(self):

		self.scale_data = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=30, to=60, resolution=30)
		self.scale_data.pack()
		#self.scale_data.place(x=self.x/5, y=self.y*4/8 +25)


		self.scale_volume = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=0, to=100, resolution=1)
		self.scale_volume.pack()
		#self.scale_volume.place(x=self.x*3/5, y=self.y*4/8 +25)

	def updatePos(self):
		if self.x != self.window.winfo_width() or self.y != self.window.winfo_height() :
			self.x = self.window.winfo_width()
			self.y = self.window.winfo_height()

			self.label_title.place(height=self.y /4, width=self.x )

			self.input_name.place(x= self.x / 5, y =  self.y / 4)
			self.input_surname.place(x=self.x *3/5, y= self.y /4)

			self.button_upload.place(x= self.x/5	,  y= self.y * 4/6)
			self.button_synthesis.place(x=self.x * 3/5, y=self.y * 4/6)
			self.button_start.pack(pady = 30 ,side=BOTTOM)

			self.label_data.place(x=self.x/5 +35, y=self.y*2/6 )
			self.label_image.place(x=self.x/5 +35, y=self.y*3/7)
			self.label_sec.place(x=self.x/5, y=self.y*4/8)
			self.label_speech.place(x=self.x* 3/5, y=self.y*4/8)

			self.data_check.place(x=self.x/5, y=self.y*2/6)
			self.graph_check.place(x=self.x/5, y=self.y*3/7)

			self.scale_data.place(x=self.x/5, y=self.y*4/8 +25)
			self.scale_volume.place(x=self.x*3/5, y=self.y*4/8 +25)

			self.list.place (x=self.x* 2/5, y=self.y*2/8 +25)
			#app.input_name.place(x= self.x / 5, y =  self.y / 4)

	def repertoiredetravail(self):
		self.repfic = filedialog.askopenfilename(title="Ouvrir le fichier:", initialdir=self.rep,
						initialfile=self.fic, filetypes = [("All", "*"),("Fichiers Python","*.py;*.pyw")])
		if len(self.repfic) > 0:
			self.rep=os.path.dirname(self.repfic)
			self.fic=os.path.basename(self.repfic)

	def upload(self):
		y = self.list.curselection()
		print(y)
		self.repertoiredetravail()

		load = Image.open(self.repfic)
		render = ImageTk.PhotoImage(load)
		#img = Label(self.im, image=render)
		#ça marche pas et je sais pas pk
		img = Label(self.window, image=render)

		img.image = render
		img.place(x=0, y=0)



def start_experimentation():
	expe = Experimentation()
	nbNoneConcecutif = 0
	while True:

		# We get a new frame from the webcam
		_, frame = webcam.read()
		# We send this frame to GazeTracking to analyze it
		gaze.refresh(frame)
		frame = gaze.annotated_frame()
		left_pupil = gaze.pupil_left_coords()
		right_pupil = gaze.pupil_right_coords()
		ratioX =  gaze.horizontal_ratio()
		ratioY = gaze.vertical_ratio()
		print('RATION X' + str(ratioX) + ' RATIO Y :' + str(ratioY))
		print('EYE  X' + str(left_pupil) + ' EYE Y :' + str(right_pupil))

		if(ratioX != None and ratioY != None):
			expe.paint_eye_point(1.0 - ratioX,ratioY)
			nbNoneConcecutif = 0
		else :
			if  nbNoneConcecutif >30000:
				nbNoneConcecutif = 0
				expe = Experimentation()
			nbNoneConcecutif += 1

		expe.window.update_idletasks()
		expe.window.update()





def callback(*args):
	#print(app.variable)
	app.button_start.configure(text="The selected item is {}".format(app.variable.get()))




##### MAIN ########

# afficher la fenêtre
app = Application()

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)


pro = Protocole("test")

while True:
	app.window.update_idletasks()
	app.window.update()
	app.updatePos()

