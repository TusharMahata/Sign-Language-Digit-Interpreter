import cv2 as cv
import HandTrackingModule as htm

cap = cv.VideoCapture(0)
detector = htm.handDectector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    fingerNum = 0
    signNum = 0

    #print(lmList)
    if len(lmList) !=0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        #fingerNum = fingers.count(1)
        if fingers[1] == 1 and fingers[0]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
            signNum = 1
        elif fingers[1] == 1 and fingers[0]==0 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
            signNum = 2
        elif fingers[1] == 1 and fingers[0]==1 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
            signNum = 3
        elif fingers[1] == 1 and fingers[0]==0 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            signNum = 4
        elif fingers[1] == 1 and fingers[0]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            signNum = 5
        elif fingers[1] == 1 and fingers[0]==0 and fingers[2]==1 and fingers[3]==1 and fingers[4]==0:
            signNum = 6
        elif fingers[1] == 1 and fingers[0]==0 and fingers[2]==1 and fingers[3]==0 and fingers[4]==1:
            signNum = 7
        elif fingers[1] == 1 and fingers[0]==0 and fingers[2]==0 and fingers[3]==1 and fingers[4]==1:
            signNum = 8
        elif fingers[1] == 0 and fingers[0]==0 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            signNum = 9

    #print(fingerNum)
    cv.putText(img, str(int(signNum)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)


    cv.imshow('Interpreter', img)
    cv.waitKey(1)