from tkinter import *
from experimentation import Experimentation
from tkinter import filedialog
from tkinter import PhotoImage
from speech import Speech
from calibration import *
#sudo apt-get install python3-pil python3-pil.imagetk
import os
import PIL
from PIL import ImageTk
from PIL import Image
from nouveauProtocole import *
from opendata import *
from graph import Graph
# pip install pillow
#pip install seaborn
# creation fenêtre


class Application :

	def __init__(self,expe,graph,window):

		self.experimentation = expe
		self.graphe = graph
		self.rep=os.getcwd()
		self.fic = ""
		self.repfic = ""
		#im = self.repertoiredetravail()

		self.window = window
		self.image = ImageTk.PhotoImage(master=self.window ,file= "data/pictures/background.jpg")
		self.label1 = Label(self.window, image = self.image)
		self.label1.pack()
		self.label1.place(x = 0, y = 0)

		#self.im = Tk()
		# self.window.attributes('-alpha',0.5)
		self.window.wm_attributes('-alpha',0.5)

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

		#self.window.config(background='#4C4B4B')

		self.label_title = Label()
		self.input_name = Entry()
		self.input_surname = Entry()

		self.button_upload = Button()
		#self.button_synthesis = Button()
		self.button_start = Button()
		self.button_add = Button()

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

		self.window.update_idletasks()
		self.window.update()
		self.updatePos()
		self.window.mainloop()



	def create_widgets(self):
		#self.creatBg()
		self.create_title()
		self.create_buttons()
		self.create_labels()
		self.create_checkboxs()
		self.create_scales()
		self.create_multiple()

		self.updatePos()
	def creatBg(self):
		image = ImageTk.PhotoImage(master=self.window ,file= "data/pictures/background.jpg")
		self.label1 = Label(self.window, image = image)
		self.label1.pack()
		self.label1.place(x = 0, y = 0)

	def create_title(self):

		# ajout du titre
		self.label_title = Label(self.window, text="Experimentation parameters",font=("Arial", 40),bg="#325261")
		self.label_title.pack()
		self.label_title.place(height= 50, width=self.x/2 )
	def create_buttons(self):

		# ajout champ de saisie
		self.input_name = Entry(self.window)
		self.input_name.insert(0, "Name")
		#self.input_name.place(x= self.x / 5, y =  self.y / 4)

		self.input_surname = Entry(self.window)
		self.input_surname.insert(0, "Surname")
		self.input_surname.pack()
		#self.input_surname.place(x=self.x *3/5, y= self.y /4)

		self.button_upload = Button(self.window, text="Choix du périphérique d'eye tracking")
		self.button_upload.pack()
		#self.button_upload.place(x= self.x/5	,  y= self.y * 4/6)

		#self.button_synthesis = Button(self.window, text="Speech Synthesis question")
		#self.button_synthesis.pack()
		#self.button_synthesis.place(x=self.x * 3/5, y=self.y * 4/6)

		self.button_add = Button(self.window, text="Add protocole",command=lambda : nouveauProtocole(self))
		self.button_add.pack()

		self.button_start = Button(self.window, text="Start experimation",command=self.launch_an_experimentation)
		#self.button_start.pack(pady = 30 ,side=BOTTOM)


	def create_labels(self):

		# ajout checkbox
		self.label_data = Label(self.window, text="Save data", font=(
			"Arial", 12))
		#self.label_data.place(x=self.x/5 +35, y=self.y*2/6 )



		self.label_image = Label(self.window, text="Save graph image",
						   font=("Arial", 12))
		#self.label_image.place(x=self.x/5 +35, y=self.y*3/7)


		self.label_sec = Label(self.window, text="Data per second",
				   font=("Arial", 12))
		self.label_sec.pack()
		#self.label_sec.place(x=self.x/5, y=self.y*4/8)

		#self.label_speech = Label(self.window, text="Volume speech synthesis",font=("Arial", 12), bg='#4C4B4B', fg='white')
		#self.label_speech.pack()
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

		x = repucProtocoles()
		self.list = Listbox(self.window, selectmode = "multiple",bg="white",selectbackground = "green",height=min(len(x) +1,10) )
		self.list.pack()

		for each_item in range(len(x)):
			self.list.insert(END, x[each_item])
			self.list.activate(each_item)

	def updateList(self,name):
		size = self.list.size()
		self.list.insert(END, name)
		self.list.activate(size)
		#self.list.pack()
		print(name)
	def create_scales(self):

		self.scale_data = Scale(self.window, bg='#4C4B4B', orient=HORIZONTAL,from_=30, to=60, resolution=30)
		self.scale_data.pack()
		#self.scale_data.place(x=self.x/5, y=self.y*4/8 +25)


		#self.scale_volume  = Scale(self.window,from_ = 0,to = 100,orient = HORIZONTAL ,resolution = 1)
		#self.scale_volume.pack()
		#self.scale_volume.place(x=self.x*3/5, y=self.y*4/8 +25)



	def updatePos(self):
		if self.x != self.window.winfo_width() or self.y != self.window.winfo_height() :
			print(self.x , ' ' , self.y)
			self.x = self.window.winfo_width()
			self.y = self.window.winfo_height()
			self.label1.place(x = 0, y = 0)
			self.label_title.place(x= self.x /4, y=self.y /10 )

			self.input_name.place(x= self.x / 5, y =  self.y / 4)
			self.input_surname.place(x=self.x *3/5, y= self.y /4)

			self.button_upload.place(x= self.x/5	,  y= self.y * 4/6)
			#self.button_synthesis.place(x=self.x * 3/5, y=self.y * 4/6)
			self.button_add.place(x=self.x * 3/5, y=self.y * 4/6)
			self.button_start.pack(pady = 30 ,side=BOTTOM)

			self.label_data.place(x=self.x/5 +35, y=self.y*2/6 )
			self.label_image.place(x=self.x/5 +35, y=self.y*3/7)
			self.label_sec.place(x=self.x/5, y=self.y*4/8)
			#self.label_speech.place(x=self.x* 3/5, y=self.y*4/8)

			self.data_check.place(x=self.x/5, y=self.y*2/6)
			self.graph_check.place(x=self.x/5, y=self.y*3/7)

			self.scale_data.place(x=self.x/5, y=self.y*4/8 +25)
			#self.scale_volume.place(x=self.x*3/5, y=self.y*4/8 +25)

			self.list.place (x=self.x* 2/5, y=self.y*2/8 +25)
			#app.input_name.place(x= self.x / 5, y =  self.y / 4)


	# def repertoiredetravail(self):
	# 	self.repfic = filedialog.askopenfilename(title="Ouvrir le fichier:", initialdir=self.rep,
	# 					initialfile=self.fic, filetypes = [("All", "*"),("Fichiers Python","*.py;*.pyw")])
	# 	if len(self.repfic) > 0:
	# 		self.rep=os.path.dirname(self.repfic)
	# 		self.fic=os.path.basename(self.repfic)



	# def upload(self):
	# 	y = self.list.curselection()
	# 	print(y)
	# 	self.repertoiredetravail()

	# 	load = Image.open(self.repfic)
	# 	render = ImageTk.PhotoImage(load)
	# 	#img = Label(self.im, image=render)
	# 	#ça marche pas et je sais pas pk
	# 	img = Label(self.window, image=render)

	# 	img.image = render
	# 	img.place(x=0, y=0)

	def launch_an_experimentation(self):
		#self.graphe.readFile("Troll")
		calibration = Calibration()
		calibration.start_calibration()
		for i in range(self.list.size()):
			if self.list.selection_includes(i) == 1:
				self.experimentation.start_experimentation(self.input_name.get(),str(self.list.get(i)),calibration,self.list.get(i))

		self.graphe.readFile(self.input_name.get())
		#self.experimentation.start_experimentation(self.input_name.get(),'test')




# def callback(*args):
# 	#print(app.variable)
# 	application.button_start.configure(text="The selected item is {}".format(application.variable.get()))


##### MAIN ########

# afficher la fenêtre



expe = Experimentation()
graph = Graph()
window = Tk()
application = Application(expe,graph,window)



# while True:
# 	application.window.update_idletasks()
# 	application.window.update()
#
