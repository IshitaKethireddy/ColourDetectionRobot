import cv2
import numpy as np

cap = cv2.VideoCapture('Video.mp4')

while True:
  
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Green Color
    lowg = np.array([40, 50, 50])
    highg = np.array([80, 255, 255])
    maskg = cv2.inRange(hsv,lowg,highg)
    res_g = cv2.bitwise_and(frame, frame, mask = maskg)

    
    # Blue Color
    lowb = np.array([100, 50, 50])
    highb = np.array([140, 255, 255])
    image_mask = cv2.inRange(hsv, lowb, highb)
    output = cv2.bitwise_and(frame, frame, mask = image_mask)
    
    # Red Color
    low = np.array([140, 150, 0])
    high = np.array([180, 255, 255])
    maskr = cv2.inRange(hsv,low,high)
    res = cv2.bitwise_and(frame, frame, mask = maskr)

    #cv2.imshow("Original", frame)
    #cv2.imshow("Mask", image_mask)#in black&white
    cv2.imshow("blue", output)
    cv2.imshow("red", res)
    cv2.imshow("green", res_g)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
