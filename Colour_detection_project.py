import cv2

cap=cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,720)

while True:
    suc,img=cap.read()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    height,width,channel=img.shape

    x=width//2
    y=height//2

    pixel_center=img_hsv[y,x]
    print(pixel_center)
    hue_value=pixel_center[0]
    sat_value=pixel_center[1]
    val_value=pixel_center[2]
    color= "NULL"
    if sat_value<20 and val_value>70:
        color="WHITE"
    elif sat_value>10 and val_value<70:
        color="BLACK"
    elif hue_value<5:
        color="RED"
    elif hue_value<22:
        color="ORANGE"
    elif hue_value<33:
        color="YELLOW"
    elif hue_value<70:
        color="GREEN"
    elif hue_value<131:
        color="BLUE"
    elif hue_value<145:
        color="VIOLET"
    elif hue_value<165:
        color="PINK"
    else:
        color="RED"

    center_bgr=img[y,x]
    b,g,r=int(center_bgr[0]),int(center_bgr[1]),int(center_bgr[2])

    cv2.putText(img,color,(50,100),0,3,(b,g,r),5)
    cv2.circle(img,(x,y),5,(252,150,22),3)

    cv2.imshow("COLOUR DETECTED IMAGE",img)
    if cv2.waitKey(1) == ord('q'):
        break

