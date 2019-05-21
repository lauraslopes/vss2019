from scipy.spatial import distance as dist
from collections import OrderedDict
import cv2 as cv
import numpy as np
import random as rng

lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80)} #assign new item lower['blue'] = (93, 10, 0)
#upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255), 'orange':(20,255,255)}
upper = {'orange':(20,255,255)}
cores = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217), 'orange':(0,140,255)}

def shapeSegmentation(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, thresh=cv.threshold(gray,127,255,1)
    
    contours = cv.findContours(thresh.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]

    for cnt in contours:
        ########FAZ CLASSIFICACAO DE COR (LENTO)
        ccc = colorClassificationS(img, cnt)
        ########DESLIGA CLASSIFICACAO DE COR
        #ccc = 'test'
        if (str(ccc) != 'None'):
            area = cv.contourArea(cnt)
            if area < 60000:
                epsilon = 0.1 * cv.arcLength(cnt,True)
                approx = cv.approxPolyDP(cnt, epsilon, True)
                #cv.drawContours(img,[cnt],0,(0, 255, 0),-1)
                
                leng = len(approx)
                if (leng >= 2 and leng <= 4):
                    #color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
                    color = (0, 255, 0)
                    #cv.drawContours(img,[cnt],0,color,-1)
                    
                    M=cv.moments(cnt)
                    if (M['m00'] != 0.0):
                        cx=int(M['m10']/M['m00'])
                        cy=int(M['m01']/M['m00'])
                        
                        if (str(ccc) == 'blue'):
                            text = 'robo'
                        elif (str(ccc) == 'orange'):
                            text = 'bola'
                        else:
                            text = 'objeto ' + str(ccc)
                        cv.putText(img,text,(cx-50,cy),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
                    x,y,w,h = cv.boundingRect(cnt)
                    cv.rectangle(img,(x,y),(x+w,y+h),color,2)
                
def colorClassificationS(img, cnt):
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv.drawContours(mask, [cnt], -1, 255, -1)
    mask = cv.erode(mask, None, iterations=2)
    
    masked = cv.bitwise_and(img, img, mask = mask)
    
    hsv = cv.cvtColor(masked, cv.COLOR_BGR2HSV) 
    
    for key, value in upper.items():
        #kernel = np.ones((9,9),np.uint8)
        mask2 = cv.inRange(hsv, lower[key], upper[key])
        #mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        #mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        cnts = cv.findContours(mask2.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
       
        if len(cnts) > 0:
            return key

def colorClassification(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, thresh=cv.threshold(gray,127,255,1)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
    for key, value in upper.items():
        mask = cv.inRange(hsv, lower[key], upper[key])

        cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
       
        if len(cnts) > 0:
            c = max(cnts, key=cv.contourArea)
            M=cv.moments(c)
            if (M['m00'] != 0.0):
                cx=int(M['m10']/M['m00'])
                cy=int(M['m01']/M['m00'])

          
                if (str(key) == 'orange'):
                	cv.putText(img,'bola',(cx-50,cy),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(img,(x,y),(x+w,y+h),cores[key],2)

def main():
    ############# IMAGEM
    '''img = cv.imread('campo2.png')
    #shapeSegmentation(img)
    colorClassification(frame)
    cv.imshow('frame', img)
    cv.waitKey(0)'''
    
    #################### OU VIDEO
    
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #shapeSegmentation(frame)
        colorClassification(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(25) == ord('q'):
            break
    cap.release()
    
    ######################
    
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    main()
