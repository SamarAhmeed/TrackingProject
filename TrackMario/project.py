import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from moviepy.editor import VideoFileClip
from IPython.display import HTML
#outfile='output1.mp4'


def trackTemplate(frame,temp2,temp3,temp4):
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #ssd =cv2.matchTemplate(grayFrame,temp1,method=cv2.TM_SQDIFF_NORMED)
    ssd2=cv2.matchTemplate(grayFrame,temp2,method=cv2.TM_SQDIFF_NORMED)
    ssd3=cv2.matchTemplate(grayFrame,temp3,method=cv2.TM_SQDIFF_NORMED)
    ssd4=cv2.matchTemplate(grayFrame,temp4,method=cv2.TM_SQDIFF_NORMED)
    #ssd5=cv2.matchTemplate(grayframe,temp5,method=cv2.TM_SQDIFF_NORMED)
    idx=4
    #minval,mxval,minLoc,maxLoc = cv2.minMaxLoc(ssd)
    minval2, mxval, minLoc2, maxLoc = cv2.minMaxLoc(ssd2)
    minval3, mxval, minLoc3, maxLoc = cv2.minMaxLoc(ssd3)
    minval4, mxval, minLoc4, maxLoc = cv2.minMaxLoc(ssd4)
    #minval5, mxval, minLoc5, maxLoc = cv2.minMaxLoc(ssd5)
    #print(minval2, minval3, minval4)

    if(minval2>.08):
        minval2=1e12
    if(minval3>.087):
        minval3=1e12
    if(minval4>.1):
        minval4=1e12
    #if(minval>.1):
    #    minval=1e12q
    [minval,minLoc,idx]=min([minval2,minLoc2,1],[minval3,minLoc3,2],[minval4,minLoc4,3])
    if(minval==1e12):
        return frame

    x, y = minLoc # minLoc is a point (x, y)
    #print(idx,minval,minLoc)
    if idx==0 or idx == 3:
         cv2.rectangle(frame, (x - 20, y), (x + 70, y + 80), color=[255, 255, 0], thickness=2)
    elif idx==1 or idx == 2 :
        cv2.rectangle(frame, (x - 10, y - 10), (x + 80, y + 150), color=[255, 255, 0], thickness=2)
    return frame

#exit('all')
small1=cv2.imread('frame0.jpg')
grayframe1=cv2.cvtColor(small1,cv2.COLOR_RGB2GRAY)
small_head2=grayframe1[870:920,520:550]
#print(small_head2)

bigframe=cv2.imread('frame628.jpg')
biggrayframe=cv2.cvtColor(bigframe,cv2.COLOR_RGB2GRAY)
big_head=biggrayframe[795:850,620:695]


bigframeR=cv2.imread('frame660.jpg')
biggrayframeR=cv2.cvtColor(bigframeR,cv2.COLOR_RGB2GRAY)
big_headR=biggrayframeR[800:855,785:850]
#cv2.imshow('x',big_headR)
#cv2.waitKey(0)
#cv2.destroyWindow('x')
#exit(0)
#ssd=cv2.matchTemplate(biggrayframe,big_head,method=cv2.TM_SQDIFF)
#x,y=cv2.minMaxLoc(ssd)[2]
#cv2.rectangle(bigframe,(x-10,y-10),(x+80,y+150),color=[255,255,0],thickness=2)

fireframe=cv2.imread('frame2856.jpg')
grayfire=cv2.cvtColor(fireframe,cv2.COLOR_RGB2GRAY)
fire_head=grayfire[795:850,880:950]

cap = cv2.VideoCapture('smb.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output3.avi',fourcc,30.0,(1920,1080))
count=0
while(cap.isOpened()):
#for i in range(900,3534):
    #currentframe=cv2.imread('frame%d.jpg'%i)
    x,currentframe=cap.read()
    if not x :
        break
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    trackTemplate(currentframe,big_head,fire_head,small_head2)
    #cv2.imshow('tracking',currentframe)
    #break
    out.write(currentframe)
    print(count)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # hold 'q' to quit the loop early
        break
    count += 1

#cv2.waitKey(0)
out.release()
cap.release()
#cv2.destroyWindow('tracking')