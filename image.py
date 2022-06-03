import numpy as np
import numpy.random as rand
import cv2
import math
img=cv2.imread("Cr7.png",0)
order=int(math.sqrt(img.size))
matrix=img.copy()
for i in range(order):
    for y in range(order):
        matrix[i][y]=int(round(img[i][y]/255))
def flip(order,probability,matrix):
    flip=matrix.copy()
    n=np.random.randint(order,size=(int(order*order*probability),2))
    for x in n:
        i=x[0]
        j=x[1]
        if flip[i][j] == 0:
            flip[i][j]=1
        elif flip[i][j] == 1:
            flip[i][j]=0
    return(flip)
for i in range(1,10):
    er=flip(order,0.5,matrix)
    er=er*255
    cv2.imwrite("Samples/50_perc/error{num}.png".format(num=i),er)