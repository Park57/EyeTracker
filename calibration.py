import os
import time
import cv2
from tkinter import *
from speech import Speech
from gaze_tracking import GazeTracking


class Calibration :

    # Constructor
    def __init__(self):
        self.window = Tk()
        self.width_window = self.window.winfo_screenwidth()
        self.height_window  = self.window.winfo_screenheight()

        # personnalisation de la fenêtre

        self.window.title("Calibration")
        self.window.geometry(str(self.width_window )+"x"+str(self.height_window ))
        self.window.minsize(480, 360)
        #self.window.iconbitmap("data/logo.ico")

        self.window.config(background='#FFFFFF')
        self.canvas = Canvas(self.window,width = self.width_window,height=self.height_window)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.hide_window()


    #Method to hide the window
    def hide_window(self):
        self.window.withdraw()

    #Method to show the window
    def show_window(self):
        self.window.update()
        self.window.deiconify()

    #Method to draw a point
    def draw_point(self,x,y):
        self.canvas.create_oval(x+20, y+20, x-20, y-20, fill="#FF0000")
        self.window.update_idletasks()
        self.window.update()

    def start_calibration (self):
        speech = Speech()


        calibration.show_window()

        self.draw_point(100,100)
        time.sleep(1)
        self.draw_point(self.width_window - 200,100)
        time.sleep(1)
        self.draw_point(self.width_window -200,self.height_window-150)
        time.sleep(1)
        self.draw_point(100,self.height_window-150)
        time.sleep(1)
        self.draw_point(self.width_window/2 -50,self.height_window/2 -50)

        #Les listes avec les points
        listXleftPointHautDroit = []
        listYleftPointHautDroit= []

        listXleftPointHautGauche = []
        listYleftPointHautGauche= []

        listXleftPointBasGauche = []
        listYleftPointBasGauche = []


        #Timer variables
        maxTime = 5
        tic = time.perf_counter()
        toc = time.perf_counter()




        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)

        speech.speakSentence('POINT HAUT GAUCHE !', 'PHD')
        time.sleep(2)
        #Collecte point HAUT GAUCHE
        #We collect data until maxTime ( seconds )
        while toc - tic < maxTime:
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None :
                x,y = gaze.pupil_left_coords()
                listXleftPointHautGauche.append(x)
                listYleftPointHautGauche.append(y)
            right_pupil = gaze.pupil_right_coords()

            toc = time.perf_counter()

        speech.speakSentence('POINT HAUT DROIT !', 'PHD')
        time.sleep(2)

        #Point HAUT DROIT
        maxTime = 5
        tic = time.perf_counter()
        toc = time.perf_counter()
        while toc - tic < maxTime:
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None :
                x,y = gaze.pupil_left_coords()
                listXleftPointHautDroit.append(x)
                listYleftPointHautDroit.append(y)
            right_pupil = gaze.pupil_right_coords()

            toc = time.perf_counter()

        speech.speakSentence('POINT BAS DROITE !', 'PHD')
        time.sleep(2)

        #Point BAS GAUCHE
        maxTime = 5
        tic = time.perf_counter()
        toc = time.perf_counter()
        while toc - tic < maxTime:
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None :
                x,y = gaze.pupil_left_coords()
                listXleftPointBasGauche.append(x)
                listYleftPointBasGauche.append(y)
            right_pupil = gaze.pupil_right_coords()

            toc = time.perf_counter()

        self.xValuePHG = max(listXleftPointHautGauche,key=listXleftPointHautGauche.count)
        self.yValuePHG = max(listYleftPointHautGauche,key=listYleftPointHautGauche.count)
        print("Calibrage pour point (100,100) : oeil gauche : ("+str(self.xValuePHG)+","+str(self.yValuePHG)+")")

        self.xValuePHD = max(listXleftPointHautDroit,key=listXleftPointHautDroit.count)
        self.yValuePHD = max(listYleftPointHautDroit,key=listYleftPointHautDroit.count)
        print("Calibrage pour point (1800,100) : oeil gauche : ("+str(self.xValuePHD)+","+str(self.yValuePHD)+")")

        self.xValuePBG = max(listXleftPointBasGauche,key=listXleftPointBasGauche.count)
        self.yValuePBG = max(listYleftPointBasGauche,key=listYleftPointBasGauche.count)
        print("Calibrage pour point (100,800) : oeil gauche : ("+str(self.xValuePBG)+","+str(self.yValuePBG)+")")


        calibrageX = 1700/abs(self.xValuePHG - self.xValuePHD)
        calibrageY = 800/abs(self.yValuePHG - self.yValuePBG)
        print("Calibrage x : "+ str(calibrageX))
        print("Calibrage y :" + str(calibrageY))

        while True :
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None :
                x,y = gaze.pupil_left_coords()
                xPoint = (x - self.xValuePHG) * calibrageX
                yPoint = (y - self.yValuePHG) * calibrageY
                self.draw_point(-xPoint,yPoint)
                print("New Point : (" +str(-xPoint)+","+str(yPoint)+")" )

if __name__ == "__main__":

    calibration = Calibration()
    calibration.start_calibration()



