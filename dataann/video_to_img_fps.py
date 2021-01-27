import os
import cv2

savepath = './asaved/'

if not os.path.exists(savepath):
    os.makedirs(savepath)


videopath = './a/'

check = 0
for filename in os.listdir(videopath):
    check +=1
    imgname = filename.split('.')[0]
    
    cap= cv2.VideoCapture(videopath + filename )
    fps = cap.get(cv2.CAP_PROP_FPS)
    nframen = int(fps // 5)  
    i = 0
    print(fps,nframen)
    sdir = savepath + imgname 
    spir = sdir + '/birdydrone' + str(check) + 'A_'
    if not os.path.exists(sdir):
        os.makedirs(sdir)
    
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%nframen == 0:
            cv2.imwrite( spir +str(i)+'.jpg',frame)
        i+=1
        

cap.release()
cv2.destroyAllWindows()
            
        
                
