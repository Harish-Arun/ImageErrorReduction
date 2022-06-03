import numpy as np
import numpy.random as rand
import cv2
import math
errorarray= []
for i in range(1,10):
    img=cv2.imread("Samples/5_perc/error{num}.png".format(num=i),0)
    order=int(math.sqrt(img.size))
    errorarray.append(img)
res=np.zeros([order,order], dtype=int)

#R3
for x in range(3):
    for i in range(order):
        for j in range(order):
            res[i][j]=res[i][j]+(errorarray[x][i][j]/255)
for i in range(order):
    for j in range(order):
        res[i][j]=int(round(res[i][j]/3))

R3=res*255
cv2.imwrite("Samples/5_perc/R3.png",R3)

#R5
for x in range(5):
    for i in range(order):
        for j in range(order):
            res[i][j]=res[i][j]+(errorarray[x][i][j]/255)
for i in range(order):
    for j in range(order):
        res[i][j]=int(round(res[i][j]/5))

R5=res*255
cv2.imwrite("Samples/5_perc/R5.png",R5)

#R7
for x in range(7):
    for i in range(order):
        for j in range(order):
            res[i][j]=res[i][j]+(errorarray[x][i][j]/255)
for i in range(order):
    for j in range(order):
        res[i][j]=int(round(res[i][j]/7))

R7=res*255
cv2.imwrite("Samples/5_perc/R7.png",R7)

#R9
for x in range(9):
    for i in range(order):
        for j in range(order):
            res[i][j]=res[i][j]+(errorarray[x][i][j]/255)
for i in range(order):
    for j in range(order):
        res[i][j]=int(round(res[i][j]/9))

R9=res*255
cv2.imwrite("Samples/5_perc/R9.png",R9)