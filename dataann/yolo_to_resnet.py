imagefolder = './birddrone_img/'
labelfolder = './birddrone_label/'

import os
import pandas
import cv2
import numpy as np

clsname = 'bird_drone'
filecsv = './filecsv.csv'
f = open(filecsv, 'w')

def readboxyolo5(labelpath,imgn,image1):
    height, width, channels = image1.shape
    f = open(labelpath + imgn + '.txt', 'r')

    bbox= []

    line = f.readline()
    while line:
        # reading yolov5 format
        linelist = line.split(' ')
        objcls = linelist[0]
        objx1 = linelist[1]
        objx2 = linelist[2]
        objx3 = linelist[3]
        objx4 = linelist[4]
        x1 = (float(objx1) - 0.5 * float(objx3)) * width
        y1 = (float(objx2) - 0.5 * float(objx4)) * height
        x2 = (float(objx1) + 0.5 * float(objx3)) * width
        y2 = (float(objx2) + 0.5 * float(objx4)) * height
        z = float(objcls)
        x = np.array([x1, y1, x2, y2, z])
        bbox.append(x)
        # bbox.append([x1 + ' ' + y1 + ' ' + x2 + ' ' + y1 + ' ' + objcls   ])
        # use realine() to read next line
        line = f.readline()
    f.close()
    bbox = np.array(bbox)
    return bbox
    
count = 0
for imgname in os.listdir(imagefolder):
    count += 1

    #if count == 10:
    #    break

    imgn = imgname.split('.')[0]
    image1 = cv2.imread(imagefolder + imgname)
    bbox1 = readboxyolo5(labelfolder, imgn, image1)
    #print(bbox1)
    bbx,bby = bbox1.shape
    
    #print(bbx,bby)
    for i in range(bbx):
        '''
        tag = int( bbox1[i,4] )
        if tag == 0:
            clsname = 'Drone'
        elif tag== 1:
            tagname = 'Bird'
        else:
            print('unknownlabel')
            continue
        
        '''
        
        
        txtline = imgname + ',' + str(int(bbox1[i,0])) + ',' + str(int(bbox1[i,1])) + ',' + str(int(bbox1[i,2])) + ',' + str(int(bbox1[i,3])) + ',' + clsname + '\n'   
        #print(imgname + ',' + str(int(bbox1[i,0])) + ',' + str(int(bbox1[i,1])) + ',' + str(int(bbox1[i,2])) + ',' + str(int(bbox1[i,3])) + ',' + clsname + '\n' )  
        f.write(txtline)
        #print(txtline)
f.close()



#########
#check non annotated images
count1 = 0
for imgname in os.listdir(imagefolder):
    count += 1

    #if count == 10:
    #    break

    imgn = imgname.split('.')[0]
    image1 = cv2.imread(imagefolder + imgname)
    bbox1 = readboxyolo5(labelfolder, imgn, image1)
    #print(bbox1)
    bbx = bbox1.shape
    if bbx[0] == 0:
        print(imgname)
        os.remove(imagefolder + imgname)
        os.remove(labelfolder + imgn + '.txt')
        count1 +=1
print(count1)
    
    
