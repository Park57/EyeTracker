from tkinter import *

# creation fenêtre


class Experimentation :

    def __init__(self):

        self.window = Tk()

        self.width_window = self.window.winfo_screenwidth()
        self.height_window  = self.window.winfo_screenheight()

        # personnalisation de la fenêtre

        self.window.title("Experimentation")
        self.window.geometry(str(self.width_window )+"x"+str(self.height_window ))
        self.window.minsize(480, 360)
        #self.window.iconbitmap("data/logo.ico")

        self.window.config(background='#4C4B4B')

        self.canvas = Canvas(self.window,width = self.width_window,height=self.height_window)
        self.canvas.pack(expand=YES, fill=BOTH)






    def paint_eye_point(self,point1,point2):
        python_green = "#476042"
        ###print("size : " + str(self.width_window )+ " x " + str(self.height_window) ) # debug
        x1, y1 = (point1 *self.width_window-10), (point2 *self.height_window -10)
        x2, y2 = (point1 *self.width_window+10), (point2 * self.height_window +10)
        self.canvas.create_oval(x1, y1, x2, y2, fill=python_green)
