import cv2
import time
import PoseDetectionModule as pm

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector(mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5)
while True:
    success, img = cap.read()
    img = detector.findPose(img)

    lmList = detector.findPose(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
