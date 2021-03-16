from tkinter import *

# creation fenêtre

window = Tk()

x = window.winfo_screenwidth()
y = window.winfo_screenheight()

# personnalisation de la fenêtre

window.title("My application")
window.geometry(str(x)+"x"+str(y))
window.minsize(480, 360)
window.iconbitmap("data/logo.ico")
window.config(background='#4C4B4B')


def upload():
    print("TODO ")


# ajout du titre
label_title = Label(window, text="Experimentation parameters",
                    font=("Arial", 40), bg='#4C4B4B', fg='white')
label_title.pack()
label_title.place(height=100, width=2000)

# ajout champ de saisie
input_name = Entry(window)
input_name.insert(0, "Name")
input_name.pack(side=LEFT)
input_name.place(x=50, y=250)
input_surname = Entry(window)
input_surname.insert(0, "Surname")
input_surname.pack()
input_surname.place(x=300, y=250)

# ajout checkbox
label_data = Label(window, text="Save data", font=(
    "Arial", 12), bg='#4C4B4B', fg='white')
label_data.place(x=80, y=300)

data_check = Checkbutton(window, text="", bg='#4C4B4B')
data_check.select()
data_check.pack()
data_check.place(x=50, y=300)

label_data = Label(window, text="Save graph image",
                   font=("Arial", 12), bg='#4C4B4B', fg='white')
label_data.place(x=80, y=350)


graph_check = Checkbutton(window, text="", bg='#4C4B4B')
graph_check.select()
graph_check.pack()
graph_check.place(x=50, y=350)

label_data = Label(window, text="Data per second",
                   font=("Arial", 12), bg='#4C4B4B', fg='white')
label_data.pack()
label_data.place(x=50, y=400)
scale_data = Scale(window, bg='#4C4B4B', orient=HORIZONTAL,
                   from_=30, to=60, resolution=30)
scale_data.pack()
scale_data.place(x=55, y=425)

button_upload = Button(window, text="Upload new image",command=upload)
button_upload.pack()
button_upload.place(x=50, y=500)

button_synthesis = Button(window, text="Speech Synthesis question")
button_synthesis.pack()
button_synthesis.place(x=300, y=500)


label_speech = Label(window, text="Volume speech synthesis",
                     font=("Arial", 12), bg='#4C4B4B', fg='white')
label_speech.pack()
label_speech.place(x=300, y=400)
scale_volume = Scale(window, bg='#4C4B4B', orient=HORIZONTAL,
                     from_=0, to=100, resolution=1)
scale_volume.pack()
scale_volume.place(x=325, y=425)


# afficher la fenêtre

window.mainloop()
