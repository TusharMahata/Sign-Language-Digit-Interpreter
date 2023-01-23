import cv2 as cv
import mediapipe as mp
import time


class handDectector():
    def __init__(self, mode=False, maxHands=2, modelCom=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelCom = modelCom
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelCom, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):



        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for self.handlms in self.results.multi_hand_landmarks:

                if draw:

                    self.mpDraw.draw_landmarks(img, self.handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])

                #if id == 4:
                #    cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                #if id == 8:
                 #   cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    dectector = handDectector()

    while True:
        success, img = cap.read()
        img = dectector.findHands(img)
        lmList = dectector.findPosition(img)

        if len(lmList) != 0:

            print(lmList[8])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

        cv.imshow('Image', img)
        cv.waitKey(1)

if __name__=='__main__':
    main()