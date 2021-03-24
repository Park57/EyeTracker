from tkinter import *
import cv2
from experimentation import Experimentation
from gaze_tracking import GazeTracking

# creation fenêtre


class Application :

	def __init__(self):

		self.window = Tk()

		self.x = self.window.winfo_screenwidth()
		self.y = self.window.winfo_screenheight()
		# personnalisation de la fenêtre

		self.window.title("My application")
		self.window.geometry(str(self.x)+"x"+str(self.y))
		self.window.minsize(480, 360)
		#self.window.iconbitmap("data/logo.ico")
		self.window.config(background='#4C4B4B')
		self.create_widgets()
		self.label_title = Label(self.window, text="Experimentation parameters",font=("Arial", 40), bg='#4C4B4B', fg='white')

	def create_widgets(self):

		self.create_title()
		self.create_buttons()
		self.create_labels()
		self.create_checkboxs()
		self.create_scales()


	def create_title(self):

		# ajout du titre
		self.label_title = Label(self.window, text="Experimentation parameters",
							font=("Arial", 40), bg='#4C4B4B', fg='white')
		self.label_title.pack()
		self.label_title.place(height=self.y /4, width=self.x )

	def create_buttons(self):

		# ajout champ de saisie
		input_name = Entry(self.window)
		input_name.insert(0, "Name")
		#input_name.pack(side=LEFT)
		input_name.place(x= self.x / 5, y =  self.y / 4)
		input_surname = Entry(self.window)
		input_surname.insert(0, "Surname")
		input_surname.pack()
		input_surname.place(x=self.x *3/5, y= self.y /4)

		button_upload = Button(self.window, text="Upload new image",command=upload)
		button_upload.pack()
		button_upload.place(x= self.x/5	,  y= self.y * 4/6)

		button_synthesis = Button(self.window, text="Speech Synthesis question")
		button_synthesis.pack()
		button_synthesis.place(x=self.x * 3/5, y=self.y * 4/6)

		button_start = Button(self.window, text="Start experimation",command=start_experimentation)
		button_start.pack(pady = 30 ,side=BOTTOM)


	def create_labels(self):

		# ajout checkbox
		label_data = Label(self.window, text="Save data", font=(
			"Arial", 12), bg='#4C4B4B', fg='white')
		label_data.place(x=self.x/5 +35, y=self.y*2/6 )



		label_data = Label(self.window, text="Save graph image",
						   font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_data.place(x=self.x/5 +35, y=self.y*3/7)


		label_data = Label(self.window, text="Data per second",
				   font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_data.pack()
		label_data.place(x=self.x/5, y=self.y*4/8)

		label_speech = Label(self.window, text="Volume speech synthesis",
					 font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_speech.pack()
		label_speech.place(x=self.x* 3/5, y=self.y*4/8)




	def create_checkboxs(self):

		data_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		data_check.select()
		data_check.pack()
		data_check.place(x=self.x/5, y=self.y*2/6)

		graph_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		graph_check.select()
		graph_check.pack()
		graph_check.place(x=self.x/5, y=self.y*3/7)


	def create_scales(self):

		scale_data = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=30, to=60, resolution=30)
		scale_data.pack()
		scale_data.place(x=self.x/5, y=self.y*4/8 +25)


		scale_volume = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=0, to=100, resolution=1)
		scale_volume.pack()
		scale_volume.place(x=self.x*3/5, y=self.y*4/8 +25)



def start_experimentation():
	expe = Experimentation()
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
		expe.window.update_idletasks()
		expe.window.update()




def upload():
	print("TODO ")



def update(app):
	app.x = app.window.winfo_width()
	app.y = app.window.winfo_height()
	app.label_title.pack()
	app.label_title.place(height=app.y /4, width=app.x )
	#app.input_name.place(x= self.x / 5, y =  self.y / 4)
	return app


##### MAIN ########

# afficher la fenêtre
app = Application()

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)




while True:
	app.window.update_idletasks()
	app.window.update()
	#app = update(app)
