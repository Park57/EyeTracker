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

        #FULL SCREEN MODE
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", lambda event: self.window.attributes("-fullscreen", not self.window.attributes("-fullscreen")))
        self.window.bind("<Escape>", lambda event: self.window.attributes("-fullscreen", False))
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

    #Method to calibrate on one point ( ie , get the x and y of the screen coordinate for the current eyes position)
    def calibrate_one_point(self ,point,gazeParam,webcamParam) :
        speech = Speech()

        #Les listes avec les points
        listXleft = []
        listYleft = []

        listXright = []
        listYright = []



        gaze = gazeParam
        webcam = webcamParam

        speech.speakSentence(point, 'point')
        time.sleep(2)

        #Timer variables
        maxTime = 5
        tic = time.perf_counter()
        toc = time.perf_counter()
        #Collecte point HAUT GAUCHE
        #We collect data until maxTime ( seconds )
        while toc - tic < maxTime :
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None :
                xL,yL = gaze.pupil_left_coords()
                listXleft.append(xL)
                listYleft.append(yL)
            if gaze.pupil_right_coords() != None :
                xR,yR = gaze.pupil_right_coords()
                listXright.append(xR)
                listYright.append(yR)

            toc = time.perf_counter()

        xPointR = max(listXright,key=listXright.count)
        yPointR = max(listYright,key=listYright.count)
        xPointL = max(listXleft,key=listXleft.count)
        yPointL = max(listYleft,key=listYleft.count)
        #print("Calibrage pour point " + point + " : oeil gauche : ("+str(self.xValuePHG)+","+str(self.yValuePHG)+")")
        x = (xPointR + xPointL)/2
        y = (yPointR + yPointL)/2
        return x,y


    def start_calibration (self):

        calibration.show_window()
        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)

        #Point haut droit
        self.draw_point(100,100)
        time.sleep(1)
        #print("Largeur fentre : " + str(self.width_window) + "longueur fentre : " +str(self.height_window))     #DEBUG
        #Point haut gauche
        self.draw_point(self.width_window - 100,100)
        time.sleep(1)
        #Point bas droite
        self.draw_point(self.width_window -100,self.height_window-100)
        time.sleep(1)
        #Point bas gauche
        self.draw_point(100,self.height_window-100)
        time.sleep(1)
        #Point milieu
        self.draw_point(self.width_window/2 ,self.height_window/2 )


        '''self.xValuePHD = max(listXleftPointHautDroit,key=listXleftPointHautDroit.count)
        self.yValuePHD = max(listYleftPointHautDroit,key=listYleftPointHautDroit.count)
        print("Calibrage pour point (1820,100) : oeil gauche : ("+str(self.xValuePHD)+","+str(self.yValuePHD)+")")

        self.xValuePBG = max(listXleftPointBasGauche,key=listXleftPointBasGauche.count)
        self.yValuePBG = max(listYleftPointBasGauche,key=listYleftPointBasGauche.count)
        print("Calibrage pour point (100,800) : oeil gauche : ("+str(self.xValuePBG)+","+str(self.yValuePBG)+")")
        '''

        self.xValuePHG,self.yValuePHG = self.calibrate_one_point("Point haut gauche",gaze,webcam)
        self.xValuePHD,self.yValuePBG = self.calibrate_one_point("Point haut droite",gaze,webcam)
        self.xValuePBG,self.yValuePBG = self.calibrate_one_point("Point bas gauche",gaze,webcam)

        calibrageX = (self.width_window-200)/abs(self.xValuePHG - self.xValuePHD)
        calibrageY = (self.height_window-200)/abs(self.yValuePHG - self.yValuePBG)
        #print("equal 1 "+ str( self.width_window-200))     #DEBUG
        #print("equal 2 "+ str(self.height_window-200))     #DEBUG
        print("Calibrage x : "+ str(calibrageX))
        print("Calibrage y :" + str(calibrageY))

        while True :
            # We get a new frame from the webcam
            _, frame = webcam.read()
            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            if gaze.pupil_left_coords() != None  and gaze.pupil_right_coords() != None:
                xLeftEye,yLeftEye = gaze.pupil_left_coords()
                xRightEye,yRightEye = gaze.pupil_right_coords()

                x = (xRightEye + xLeftEye)/2
                y = (yRightEye + yLeftEye)/2
                xPoint = abs(x - self.xValuePHG) * calibrageX
                yPoint = abs(y - self.yValuePHG) * calibrageY
                self.draw_point(xPoint,yPoint)
                print("New Point : (" +str(xPoint)+","+str(yPoint)+")" )

if __name__ == "__main__":

    calibration = Calibration()
    calibration.start_calibration()



