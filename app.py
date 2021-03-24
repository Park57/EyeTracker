from tkinter import *
import cv2
from experimentation import Experimentation
from gaze_tracking import GazeTracking

# creation fenêtre


class Application :

	def __init__(self):

		self.window = Tk()

		x = self.window.winfo_screenwidth()
		y = self.window.winfo_screenheight()

		# personnalisation de la fenêtre

		self.window.title("My application")
		self.window.geometry(str(x)+"x"+str(y))
		self.window.minsize(480, 360)
		#self.window.iconbitmap("data/logo.ico")

		self.window.config(background='#4C4B4B')
		self.create_widgets()

	def create_widgets(self):

		self.create_title()
		self.create_buttons()
		self.create_labels()
		self.create_checkboxs()
		self.create_scales()


	def create_title(self):

		# ajout du titre
		label_title = Label(self.window, text="Experimentation parameters",
							font=("Arial", 40), bg='#4C4B4B', fg='white')
		label_title.pack()
		label_title.place(height=100, width=2000)

	def create_buttons(self):

		# ajout champ de saisie
		input_name = Entry(self.window)
		input_name.insert(0, "Name")
		input_name.pack(side=LEFT)
		input_name.place(x=50, y=250)
		input_surname = Entry(self.window)
		input_surname.insert(0, "Surname")
		input_surname.pack()
		input_surname.place(x=300, y=250)

		button_upload = Button(self.window, text="Upload new image",command=upload)
		button_upload.pack()
		button_upload.place(x=50, y=500)

		button_synthesis = Button(self.window, text="Speech Synthesis question")
		button_synthesis.pack()
		button_synthesis.place(x=300, y=500)

		button_start = Button(self.window, text="Start experimation",command=start_experimentation)
		button_start.pack(pady = 30 ,side=BOTTOM)


	def create_labels(self):

		# ajout checkbox
		label_data = Label(self.window, text="Save data", font=(
			"Arial", 12), bg='#4C4B4B', fg='white')
		label_data.place(x=80, y=300)



		label_data = Label(self.window, text="Save graph image",
						   font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_data.place(x=80, y=350)


		label_data = Label(self.window, text="Data per second",
				   font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_data.pack()
		label_data.place(x=50, y=400)

		label_speech = Label(self.window, text="Volume speech synthesis",
					 font=("Arial", 12), bg='#4C4B4B', fg='white')
		label_speech.pack()
		label_speech.place(x=300, y=400)




	def create_checkboxs(self):

		data_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		data_check.select()
		data_check.pack()
		data_check.place(x=50, y=300)

		graph_check = Checkbutton(self.window, text="", bg='#4C4B4B')
		graph_check.select()
		graph_check.pack()
		graph_check.place(x=50, y=350)


	def create_scales(self):

		scale_data = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=30, to=60, resolution=30)
		scale_data.pack()
		scale_data.place(x=55, y=425)


		scale_volume = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=0, to=100, resolution=1)
		scale_volume.pack()
		scale_volume.place(x=325, y=425)



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





##### MAIN ########

# afficher la fenêtre
app = Application()

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)




while True:
	app.window.update_idletasks()
	app.window.update()
