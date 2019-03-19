# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:10:46 2018

@author: aro
"""

import numpy
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt

#change the pic to black and white
im= Image.open('pack_1_rec_Cor508.bmp')
imarray = numpy.array(im)
for i in range(len(imarray)):
    for j in range(len(imarray[0])):
        if imarray[i,j]>=165:
            imarray[i,j]=255
        else:
            imarray[i,j]=0
imbi=Image.fromarray(imarray)
imbi.show()

#check if the color change in specific line
x=222
len_black=numpy.array([])
len_white=numpy.array([])
change_num=numpy.array([])
countb=0
countw=0
for i in range(len(imarray)-1):
    for j in range(len(imarray[0])):
        if imarray[i,j]==0:
            if imarray[i,j]==imarray[i+1,j]:
                countb=countb+1
            else:
                len_black=numpy.append(len_black,countb)#if th
                countb=0
        if imarray[i,j]==255:
            if imarray[i,j]==imarray[i+1,j]:
                countw=countw+1
            else:
                len_white=numpy.append(len_white,countw)
                countw=0
    if imarray[(len(imarray))-1,x]==0:
        len_black=numpy.append(len_black,countb)
    else:
        len_white=numpy.append(len_white,countw)





#    if imarray[i,x]== imarray[i+1,x]:
#        if imarray[i,x]==255:
#            len_black+=1
#        elif imarray[i,x]==0:
#            len_white+=1
#    else:
#        len_black=numpy.append(len_black,0)
#        len_white=numpy.append(len_white,0)
#        print len_white
#        print len_black

#len_black=len_black[numpy.nonzero(len_black)]
#len_white=len_white[numpy.nonzero(len_white)]
print 'len_white:',len_white
print 'len_black:',len_black
#plt.figure(figsize=(8,14),dpi=80)
plt.subplot(2,2,1)
plt.hist(len_black,  facecolor="green", alpha=0.75)
plt.xlabel('length of particles (pixels)')
plt.ylabel('number of times the length appear ')
plt.title(r'Histogram of particles length')
plt.show
plt.subplot(2,2,2)
plt.hist(len_white,  facecolor="green", alpha=0.75)
plt.xlabel('length of porous (pixels)')
plt.ylabel('number of times the length appear ')
plt.title(r'Histogram of porous length')

plt.show

 #change the pic to black and white
im= Image.open('Pack_1_rec_Cor1000.bmp')
imarray = numpy.array(im)
for i in range(len(imarray)):
    for j in range(len(imarray[0,])):
        if imarray[i,j]>=165:
            imarray[i,j]=255
        else:
            imarray[i,j]=0
imbi=Image.fromarray(imarray)
imbi.show()

#check if the color change in specific line
x=222
len_black=numpy.array([])
len_white=numpy.array([])
change_num=numpy.array([])
countb=0
countw=0
for i in range(len(imarray)-1):
    if imarray[i,x]==0:
        if imarray[i,x]==imarray[i+1,x]:
            countb=countb+1
        else:
            len_black=numpy.append(len_black,countb)
            countb=0
    if imarray[i,x]==255:
        if imarray[i,x]==imarray[i+1,x]:
            countw=countw+1
        else:
            len_white=numpy.append(len_white,countw)
            countw=0
if imarray[(len(imarray))-1,x]==0:
    len_black=numpy.append(len_black,countb)
else:
    len_white=numpy.append(len_white,countw)





#    if imarray[i,x]== imarray[i+1,x]:
#        if imarray[i,x]==255:
#            len_black+=1
#        elif imarray[i,x]==0:
#            len_white+=1
#    else:
#        len_black=numpy.append(len_black,0)
#        len_white=numpy.append(len_white,0)
#        print len_white
#        print len_black

#len_black=len_black[numpy.nonzero(len_black)]
#len_white=len_white[numpy.nonzero(len_white)]
print 'len_white:',len_white
print 'len_black:',len_black

plt.subplot(2,2,3)
plt.hist(len_black,  facecolor="blue", alpha=0.75)
plt.xlabel('length of particles (pixels)')
plt.ylabel('number of times the length appear ')
plt.title(r'Histogram of particles length- pack')
plt.show
plt.subplot(2,2,4)
plt.hist(len_white,  facecolor="blue", alpha=0.75)
plt.xlabel('length of porous (pixels)')
plt.ylabel('number of times the length appear ')
plt.title(r'Histogram of porous length- pack')

plt.show
