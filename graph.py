import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
import  seaborn  as  sns
import  pandas  as  pd
from scipy.interpolate import griddata




class Graph:

    def __init__(self):
        self.test = 0



    def readFile(self,dossier,nomFichier):
        dataX = np.array([])
        dataY = np.array([])
        file = "data/sauvegarde/"+dossier+"/"+nomFichier+".txt"
        with open(file) as f:
            content = f.readlines()
        for line in content:
            coordX = re.match("^\(\d*",line)
            coordX= coordX.group()
            lengthX = len(coordX)
            coordX = coordX[1:lengthX]

            coordY = re.search(",\d*",line)
            coordY = coordY.group()
            lengthY = len(coordY)
            coordY = coordY[1:lengthY]
            dataX = np.append(dataX,int(coordX))
            dataY = np.append(dataY,int(coordY))
        print(dataX) #DEBUG
        print(dataY) #DEBUG
        
        #2D array with the coord x,y
        z = np.column_stack((dataX, dataY))

        
        plt.scatter(dataX,dataY)

        plt.title('Nuage de points représentant coordonnées X et Y du regard sur l\'écran')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('data/sauvegarde/'+dossier+'/graphique.png')
        plt.show()

        






            