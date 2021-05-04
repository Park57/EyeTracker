import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import math




class Graph:

    def __init__(self):
        self.test = 0

 
    # function who reads a file with coordinates X,Y and who creates 3 graphs
    # 1st graph is a simple graph with a point X,Y 
    # 2nd graph is the 1st graph plus arrows who indicates the gaze
    # 3rd graph is a heatmap
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
                    if(cpt == 0): # Pour la première ligne du fichier
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

                        coordY = re.search(",.\d*",line)
                        coordY = coordY.group()
                        lengthY = len(coordY)
                        coordY = coordY[1:lengthY]
                        if((int(coordX) <= width and int(coordY) <= height) and (int(coordX)  >= 0 and int(coordY) >= 0)):
                            dataX = np.append(dataX,int(coordX))
                            dataY = np.append(dataY,int(coordY))
                print(dataX)
                print(dataY)

                #2D array with the coord x,y
                z = np.column_stack((dataX, dataY))
                i = 1

                # 1st graph
                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.title('Nuage de points représentant coordonnées X et Y du regard sur l\'écran')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.show()

                # 2nd graph
                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.title('Nuage de points avec suivi du regard')
                plt.xlabel('x')
                plt.ylabel('y')
                while i < len(dataX):
                    # distance euclidienne pour n'afficher que les flèches à une certaine distance
                    if(math.sqrt(((dataX[i]-dataX[i-1])*(dataX[i]-dataX[i-1]))+(dataY[i]-dataY[i-1])*(dataY[i]-dataY[i-1]))> 100): 
                        plt.annotate('', xy=(dataX[i], dataY[i]),xytext=(dataX[i-1],dataY[i-1]),arrowprops=dict(facecolor='black',arrowstyle='->'))
                    i += 1
                plt.savefig('data/sauvegarde/'+dossier+'/graphics'+str(k)+'.png')
                k += 1
                plt.show()

                #3rd graph 
                plt.figure(1,figsize=(15,8))
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.hist2d(dataX, dataY, bins=(300, 300), cmap=plt.cm.Reds)
                plt.colorbar()
                plt.show()


        


            