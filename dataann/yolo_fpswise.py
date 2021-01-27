import os
import cv2

savepath = './resultframe1/'
annpath = './resultframe1/'
#annpath = './yoloann1/'
if not os.path.exists(savepath):
    os.makedirs(savepath)

if not os.path.exists(annpath):
    os.makedirs(annpath )
    
videopath = './train_videos/'
labelpath = './annotations/'

for filename in os.listdir(videopath):
    imgname = filename.split('.')[0]
    print(imgname)
    f = open(labelpath + imgname + '.txt', 'r')
     
    cap= cv2.VideoCapture(videopath + filename )
    fps = cap.get(cv2.CAP_PROP_FPS)
    nframen = int(fps // 5)  
    i = 0
    print(fps,nframen)
    sdir = savepath + imgname + '/'
    if not os.path.exists(sdir):
        os.makedirs(sdir)
    
    
    while(cap.isOpened()):
        
        ret, frame = cap.read()
        line = f.readline()
        flist1 = line.split(' ')
        
        if ret == False:
            break
        if len(flist1) <=1:
            break
        objno = int(flist1[1])
        if objno > 0 and i%nframen == 0:        
            cv2.imwrite(sdir + imgname + '_' +str(i) + '.jpg',frame)
            print('|', end ="")
            file = open(sdir + imgname + '_' +str(i)  + '.txt', 'w')
            
            height, width, channels = frame.shape
            
            for j in range(objno):
                
                x1 = int(flist1[2 + (5*j)])
                y1 = int(flist1[3 + (5*j)])
                if x1 < 0:
                    x1 = 0
                if y1 < 0:
                    y1 = 0
                    
                
                x2 = int(flist1[2 + (5*j)])   +  int(flist1[4 + (5*j)]) 
                y2 = int(flist1[3 + (5*j)])   +  int(flist1[5 + (5*j)])  
                
                x1 = x1/width
                x2 = x2/width
                y1 = y1 / height
                y2 = y2/ height
                cwidth = x2 -x1
                cheight = y2 - y1
                cenleft = x1 + 0.5 * (cwidth)
                centop = y1 + 0.5 * (cheight)
                cenleft = float("{:.4f}".format(cenleft))
                centop = float("{:.4f}".format(centop))
                cwidth = float("{:.4f}".format(cwidth ))
                cheight = float("{:.4f}".format(cheight) )
                #tagx = flist1[6 + (5*objno)]
                #if tagx == 'drone':
                obj_n = 0
                
                    
                file.write(str(obj_n))
                file.write(' ')
                file.write(str(cenleft))
                file.write(' ')
                file.write(str(centop))
                file.write(' ')
                file.write(str(cwidth))
                file.write(' ')
                file.write(str(cheight))
                file.write('\n')
            file.close()
        i= i + 1       
    print('\nframes',i)
