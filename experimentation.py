import os
import time
import cv2
from tkinter import *
from gaze_tracking import GazeTracking
from opendata import repucProtocoleInfo
#from opendata import *
# creation fenêtre
from PIL import ImageTk,Image
import os
class Experimentation :

    def __init__(self):
        self.VARIABLEBIDON = 0



    #A method to debug the eye tracking points
    def paint_eye_point(self,ratioX,ratioY):
        python_green = "#476042"
        ###print("size : " + str(self.width_window )+ " x " + str(self.height_window) ) # debug
        x1, y1 = (ratioX *self.width_window-10), (ratioY *self.height_window -10)
        x2, y2 = (ratioX *self.width_window+10), (ratioY * self.height_window +10)
        self.canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    #Method to draw a point
    def draw_point(self,x,y):
        self.canvas.create_oval(x+10, y+10, x-10, y-10, fill="#FF0000")
        self.window.update_idletasks()
        self.window.update()


    #Method to save the data
    def save_data(self,ratioX,ratioY,dossier,nomFichier) :
        x1, y1 = (ratioX *self.width_window-10), (ratioY *self.height_window -10)
        x2, y2 = (ratioX *self.width_window+10), (ratioY * self.height_window +10)
        x = (int)(x1+x2)/2
        y = (int)(y1+y2)/2
        file = open("data/sauvegarde/"+dossier+"/"+nomFichier,"a+")
        file.write("("+str(x)+","+str(y)+")\n")


    #Method to start an new experimentation
    def start_experimentation(self,directory,file,calibration,image = None):
        self.window = Tk()
        liste = []
        self.width_window = self.window.winfo_screenwidth()
        self.height_window  = self.window.winfo_screenheight()
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", lambda event: self.window.attributes("-fullscreen", not self.window.attributes("-fullscreen")))
        self.window.bind("<Escape>", lambda event: self.window.attributes("-fullscreen", False))

        # personnalisation de la fenêtre

        self.window.title("Experimentation")
        self.window.geometry(str(self.width_window )+"x"+str(self.height_window ))
        self.window.minsize(480, 360)
        #self.window.iconbitmap("data/logo.ico")

        self.window.config(background='#4C4B4B')

        self.canvas = Canvas(self.window,width = self.width_window,height=self.height_window)
        self.canvas.pack(expand=YES, fill=BOTH)

        if image is not None:
            nomProtocole,adressImage, temps = repucProtocoleInfo(image)
            s = os.getcwd()
            image = ImageTk.PhotoImage(master=self.window ,file= s+'/'+ adressImage)
            self.canvas.create_image(50, 50, image=image, anchor=NW)
            maxTime = int(temps)
        else:
            maxTime = 5

        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)

        nbNoneConcecutif = 0

        #Create folder if not exist , we name it with the name of the person (Name input)
        if not os.path.exists("data/sauvegarde/"+directory):
            os.makedirs("data/sauvegarde/"+directory)

        #Timer variables

        tic = time.perf_counter()
        toc = time.perf_counter()

        while toc - tic < maxTime :
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None  and gaze.pupil_right_coords() != None:
                xLeftEye,yLeftEye = gaze.pupil_left_coords()
                xRightEye,yRightEye = gaze.pupil_right_coords()

                '''x = (xRightEye + xLeftEye)/2
                y = (yRightEye + yLeftEye)/2
                xPoint = abs(x - self.xValuePHG) * calibrageX
                yPoint = abs(y - self.yValuePHG) * calibrageY'''
                xPoint,yPoint = calibration.getScreenCoord(xLeftEye,xRightEye,yLeftEye,yRightEye)
                self.draw_point(xPoint,yPoint)
                print("New Point : (" +str(xPoint)+","+str(yPoint)+")" )
                #f.write("("+str(int(xPoint))+","+str(int(yPoint))+")\n")
            toc = time.perf_counter()
        #f.close()
        ''''
        #We collect data until maxTime ( seconds )
        while toc - tic < maxTime:

            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            ratioX =  gaze.horizontal_ratio()
            ratioY = gaze.vertical_ratio()
            print('RATION X' + str(ratioX) + ' RATIO Y :' + str(ratioY))        #DEBUG
            print('EYE  X' + str(left_pupil) + ' EYE Y :' + str(right_pupil))   #DEBUG

            if(ratioX != None and ratioY != None):
                self.paint_eye_point(1.0 - ratioX,ratioY)
                self.save_data(ratioX,ratioY,directory,'EXPE_NUM_1')
                nbNoneConcecutif = 0
            else :
                if  nbNoneConcecutif >30000:
                    nbNoneConcecutif = 0
                    self = Experimentation()
                nbNoneConcecutif += 1

            self.window.update_idletasks()
            self.window.update()

            #Get the time
            toc = time.perf_counter()'''

        #We delete the experimentation variable to remove the windows (easy and lazy method, better to pass the Tk window
        #in the experimetnation constructor ) TO DO
        self.quit()


    def quit(self):
        self.window.destroy()
