import cv2 as cv
#import numpy as np
#import imutils
#import Variables

l_enemy = (-32, 129, 112)
u_enemy = (48,209,192)
max_area = 500
min_area = 150

def drawContours(cnt, img, ratio, texto):
    M = cv.moments(cnt)
    if (M['m00'] != 0.0):
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        
        cnt = cnt.astype("float")
        cnt *= ratio
        cnt = cnt.astype("int")
        cv.drawContours(img, [cnt], -1, (0, 255, 0), 2)
        cv.putText(img, texto, (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        #cv.imshow("img", img)
        #cv.waitKey(0)
        return (cX, cY)

'''def colorClassification(img, cnt):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
    mask = np.zeros(hsv.shape[:2], dtype="uint8")
    cv.drawContours(mask, [cnt], -1, 255, -1)
    mask = cv.erode(mask, None, iterations=2)
    
    res = cv.bitwise_and(hsv, hsv, mask = mask)
    
    masked = cv.inRange(res, l_enemy, u_enemy)
    
    if (np.count_nonzero(masked) > 0):
        return True
    else:
        return False

def shapeSegmentation(cnt):
    epsilon = 0.04 * cv.arcLength(cnt,True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    
    #if len(approx) >= 3:
    #    return True
    #else:
    #    return False
    return len(approx)

def findEnemy(img):
    #redimensiona a imagem para que as formas possam ser aproximadas melhor
    resized = imutils.resize(img, width=300)
    ratio = img.shape[0] / float(resized.shape[0])
    
    #um leve blur na imagem + gray + L*a*b* color spaces
    blurred = cv.GaussianBlur(resized, (5, 5), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY)[1]
    
    #procura contornos na imagem
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for cnt in cnts:
        area = cv.contourArea(cnt)
        #se o contorno tiver area minima
        #if (area > min_area and area < max_area):
            #se passou na forma
        len = shapeSegmentation(cnt)
        if (len >= 4):
            #se passou na cor entre l_enemy e u_enemy
            if (colorClassification(blurred, cnt)):
                drawContours(cnt, img, ratio, str(len))'''
        
def findEnemy2(img):
    #1. transforma imagem pra hsv 2. binariza so as partes da imagem com a cor entre hsv 3. encontra contornos
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
    mask = cv.inRange(hsv, l_enemy, u_enemy)
    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    #como os contornos sao muito pequenos e preciso fazer isso
    #1. desenha os contornos na imagem binaria 2. dilata as imagem para juntar os contornos proximos
    cv.drawContours(mask, cnts, -1, 255, -1)
    mask = cv.dilate(mask, None, iterations=2)

    #procura por contornos novamente mas agora com os 'objetos' juntos agrupados
    cntss = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    i = 0
    for cnt in cntss:
        area = cv.contourArea(cnt)
        if (area > min_area and area < max_area):
            #len = shapeSegmentation(cnt)
            #if (len >= 3):
            #print(i)
            (x, y) = drawContours(cnt, img, 1, 'inimigo')
            
            #enemy = Variables.enemiesPosition[i]
            #enemy['x'] = x
            #enemy['y'] = y
            
            i = i + 1
            if (i == 3):
                break

def main():
    #Variables.Global()
    cap = cv.VideoCapture('robos.avi')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        findEnemy2(frame)
        
        i = 0
        #for enemy in Variables.enemiesPosition:
        #    print("Inimigo= " + str(i+1) + " x= " + str(Variables.enemiesPosition[i]['x']) + " y= " + str(Variables.enemiesPosition[i]['y']))
        #    i = i + 1
        
        cv.imshow('frame', frame)
        if cv.waitKey(25) == ord('q'):
            break
    cap.release()
    
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    main()