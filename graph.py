import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import math
import seaborn as sns




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
        l = 1 # counter for files
        for element in os.listdir("data/sauvegarde/"+dossier):
            file = "data/sauvegarde/"+dossier+"/"+element
            if(file.endswith('.txt')): # we don't care about others files than .txt
                with open(file) as f:
                    content = f.readlines()
                    cpt = 0
                for line in content:
                    if(cpt == 0): # for the 1st line of thefile we get the width height of the screen
                        ex2 = re.match("\w\d*",line)
                        ex = re.match("\d*\/",line)
                        ex = ex.group()
                        ex2= ex2.group()
                        width = int(ex[0:len(ex)-1])
                        height = int(ex2[1:len(ex)])
                        cpt = 1
                    else: # for the rest of the file we get the coordinate X,Y of the gaze on the screen with regex
                        coordX = re.match("^\(\d*",line)
                        coordX= coordX.group()
                        lengthX = len(coordX)
                        coordX = coordX[1:lengthX]

                        coordY = re.search(",.\d*",line)
                        coordY = coordY.group()
                        lengthY = len(coordY)
                        coordY = coordY[1:lengthY]
                        if((int(coordX) <= width and int(coordY) <= height) and (int(coordX)  >= 0 and int(coordY) >= 0)): # we don't care about gaze out of screen
                            dataX = np.append(dataX,int(coordX))
                            dataY = np.append(dataY,int(coordY))
                i = 1

                # 1st graph
                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.title('clouds of points corresponding to the X Y coordinates of the gaze on the screen')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.savefig('data/sauvegarde/'+dossier+'/simple_graphic_image_'+str(l)+'.png')
                plt.draw()
                plt.pause(3)
                plt.close()



                # 2nd graph
                plt.figure(1,figsize=(15,8))
                plt.scatter(dataX,dataY)
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.title('point clouds with gaze tracking')
                plt.xlabel('x')
                plt.ylabel('y')
                x = 1
                while i < len(dataX):
                    # we use the Euclidean distance to display only arrows greater than 100 pixels
                    if(math.sqrt(((dataX[i]-dataX[i-1])*(dataX[i]-dataX[i-1]))+(dataY[i]-dataY[i-1])*(dataY[i]-dataY[i-1]))> 100):
                        plt.annotate('  '+str(x), xy=(dataX[i], dataY[i]),xytext=(dataX[i-1],dataY[i-1]),arrowprops=dict(facecolor='black',arrowstyle='->'))
                        x += 1
                    i += 1
                plt.savefig('data/sauvegarde/'+dossier+'/gaze_graphic_image_'+str(l)+'.png')
                plt.draw()
                plt.pause(3)
                plt.close()




                #3rd graph
                plt.figure(1,figsize=(15,8))
                plt.xlim(-50,width+100)
                plt.ylim(-50,height+100)
                plt.title('contour plot of the gaze')
                plt.xlabel('x')
                plt.ylabel('y')
                sns.kdeplot(dataX, y=dataY, cmap="Reds", shade=True, bw_adjust=.5)
                plt.savefig('data/sauvegarde/'+dossier+'/contour_plot_image_'+str(l)+'.png')
                plt.draw()
                plt.pause(3)
                plt.close()


                l +=1






