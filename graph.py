import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
import  seaborn  as  sns
import  pandas  as  pd
import os
from scipy.interpolate import griddata




class Graph:

    def __init__(self):
        self.test = 0



    def readFile(self,dossier):
        dataX = np.array([])
        dataY = np.array([])
        k = 1
        for element in os.listdir("data/sauvegarde/"+dossier):
            file = "data/sauvegarde/"+dossier+"/"+element
            if(file.endswith('.txt')):
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

                plt.figure(1,figsize=(15,8))
                plt.subplot(3,3,2)
                plt.scatter(dataX,dataY)
                plt.title('Nuage de points représentant coordonnées X et Y du regard sur l\'écran')
                plt.xlabel('x')
                plt.ylabel('y')
                i = 1
                plt.subplot(3,3,8)
                plt.scatter(dataX,dataY)

                plt.title('Nuage de points avec suivi du regard')
                plt.xlabel('x')
                plt.ylabel('y')
                while i < len(dataX):
                    print(i)
                    plt.annotate('', xy=(dataX[i], dataY[i]),xytext=(dataX[i-1],dataY[i-1]),arrowprops=dict(facecolor='black',arrowstyle='->'))
                    i += 1
                plt.savefig('data/sauvegarde/'+dossier+'/graphics'+str(k)+'.png')
                k += 1
                plt.show()


        


            