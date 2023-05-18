import cv2
import pickle

width, height = (100), (150)

posList = []

try:
    with open('CarParkpos', 'rb') as f:
        posList = pickle.load(f)
except:
    pass

def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

while True:
    img = cv2.imread('carPark.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)


    cv2.imshow('Image', img)

    cv2.setMouseCallback('Image', mouseClick)

    cv2.waitKey(1)

    with open('CarParkpos','wb') as f:
        pickle.dump(posList,f)


