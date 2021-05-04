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
                    cpt = 0
                for line in content:
                    if(cpt == 0):
                        ex2 = re.match("\w\d*",line)
                        ex = re.match("\d*\/",line)
                        ex = ex.group()
                        ex2= ex2.group()
                        width = int(ex[0:len(ex)-1])
                        height = int(ex2[1:len(ex)])
                        cpt = 1
                    else:
                        coordX = re.match("^\(\d*",line)
                        coordX= coordX.group()
                        lengthX = len(coordX)
                        coordX = coordX[1:lengthX]

                        coordY = re.search(",\d*",line)
                        coordY = coordY.group()
                        lengthY = len(coordY)
                        coordY = coordY[1:lengthY]
                        if(int(coordX) <= width and int(coordY) <= height):
                            dataX = np.append(dataX,int(coordX))
                            dataY = np.append(dataY,int(height-int(coordY)))
                        #print(dataX) #DEBUG
                        #print(dataY) #DEBUG

                print(dataX)
                print(dataY)
                #2D array with the coord x,y
                z = np.column_stack((dataX, dataY))

                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-100,width+100)
                plt.ylim(-100,height+100)
                plt.title('Nuage de points représentant coordonnées X et Y du regard sur l\'écran')
                plt.xlabel('x')
                plt.ylabel('y')
                i = 1
                plt.show()
                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-100,width+100)
                plt.ylim(-100,height+100)
                plt.title('Nuage de points avec suivi du regard')
                plt.xlabel('x')
                plt.ylabel('y')
                while i < len(dataX):
                    if(max(dataX[i],dataY[i]) - min(dataX[i],dataY[i])  > 400 or max(dataX[i-1],dataY[i-1]) - min(dataX[i-1],dataY[i-1]) > 400):
                        plt.annotate('', xy=(dataX[i], dataY[i]),xytext=(dataX[i-1],dataY[i-1]),arrowprops=dict(facecolor='black',arrowstyle='->'))
                    i += 1
                plt.savefig('data/sauvegarde/'+dossier+'/graphics'+str(k)+'.png')
                k += 1
                plt.show()
                plt.figure(1,figsize=(15,8))
                #plt.xlim(-100,width+100)
                #plt.ylim(-100,height+100)
                plt.hist2d(dataX, dataY, bins=(300, 300), cmap=plt.cm.Reds)
                plt.colorbar()
                plt.show()


        


            