from cProfile import label
import cv2
import mediapipe as mp
import pytesseract
import matplotlib.pyplot as plt
import os
import time
import dbOps as db
from tkinter import *

global try_again_counter
try_again_counter = 0
global cap
cap = cv2.VideoCapture(0)
global c
c=1
def try_again():
    root1=Tk()
    root1.title("Scan ID again")
    root1.geometry("1920x1080")
    w=Label(root1,text="Try again",font=("Courier", 30))
    w.pack()
    w.place(relx=0.5,rely=0.5,anchor=CENTER)
    root1.after(2000,lambda:root1.destroy())
    root1.mainloop()


def OCR():
    global try_again_counter
    TIMER = int(5)
    #cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('Scan ID', img)
        #k = cv2.waitKey(125)
        #if k == ord('q'):
        prev = time.time()
        while TIMER >= 0:
            ret, img = cap.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(TIMER),(200, 250), font, 7, (0, 255, 255), 4, cv2.LINE_AA)
            cv2.imshow('Scan ID', img)
            cv2.waitKey(125)
            cur = time.time()
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
        else:
            ret, img = cap.read()
            cv2.imshow('Scan ID', img)
            cv2.waitKey(2000)
            directory = r'D:\IoT'
            os.chdir(directory)
            cv2.imwrite('camera.jpeg', img)
            break
    #cap.release()
    cv2.destroyAllWindows()
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread('D:\IoT\camera.jpeg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img)
    img2char = pytesseract.image_to_string(img)
    print(img2char)
    for line in img2char.split("\n"):
        line=line.replace("5","S")
        if ("PESi" in line or "PES1" in line or "PESl" in line):
            global line1
            line1=line.replace("i", "1").replace("l", "1").replace("€", "E")
            last_chars = line1[10:]
            if ("S" in last_chars or "s" in last_chars):
                last_chars1=last_chars.replace("S", "5").replace("s", "5")
                line1 =line1.replace(last_chars,last_chars1)
            print(line1)
            length1=len(line1)
            if length1!=13:
                OCR()
            else:
                break
    
    if "PES1" not in img2char:
        print("Try again")
        global c
        print(c)
        c=c+1
        try_again()
        try_again_counter=try_again_counter+1
        if (try_again_counter<=2):
            OCR()
        else:
            start()

def squat_counter(line1):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    global counter
    counter = 0
    prev=time.time()
    stage = None
    create = None
    opname = "output.avi"
    def findPosition(image, draw=True):
    
      lmList = []
      if results.pose_landmarks:
    
          mp_drawing.draw_landmarks(
        
             image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
          for id, lm in enumerate(results.pose_landmarks.landmark):
        
              h, w, c = image.shape
              cx, cy = int(lm.x * w), int(lm.y * h)
              lmList.append([id, cx, cy])
          #cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
      return lmList
    #cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('D:\IoT\squat_video.mp4')
    with mp_pose.Pose(
    
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
      while cap.isOpened():
    
        success, image = cap.read()
        image = cv2.resize(image, (640,480))
        if not success:
        
          print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
          continue
      
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
        results = pose.process(image)
    # Draw the pose annotation on the image.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        lmList = findPosition(image, draw=True)
        #prev = time.time()
        if len(lmList) != 0:
        
          cv2.circle(image, (lmList[24][1], lmList[24][2]), 20, (0, 0, 255), cv2.FILLED)
          cv2.circle(image, (lmList[23][1], lmList[23][2]), 20, (0, 0, 255), cv2.FILLED)
          cv2.circle(image, (lmList[24][1], lmList[24][2]), 20, (0, 0, 255), cv2.FILLED)
          cv2.circle(image, (lmList[23][1], lmList[23][2]), 20, (0, 0, 255), cv2.FILLED)
          #prev = time.time()
          if ((lmList[26][2]-lmList[24][2])<=40 and (lmList[25][2]-lmList[23][2]) <=40): #Used to check if the hip joints and on the same or beloew the knee level
        
            cv2.circle(image, (lmList[24][1], lmList[24][2]), 20, (0, 255, 0), cv2.FILLED)
            cv2.circle(image, (lmList[23][1], lmList[23][2]), 20, (0, 255, 0), cv2.FILLED)
            stage = "down"
          if (lmList[24][2] and lmList[23][2] <= lmList[26][2] and lmList[25][2]) and stage == "down":
        
            stage = "up"
            counter += 1
            time.sleep(1)
            prev = time.time()
            counter2 = str(int(counter))
            print(counter)
            #os.system("echo '" + counter2 + "' | festival --tts")
        text = "{}:{}".format("Squats", counter)
        cv2.putText(image, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)
        cv2.imshow(line1, image)
        if create is None:
        
          fourcc = cv2.VideoWriter_fourcc(*'XVID')
          create = cv2.VideoWriter(opname, fourcc, 30, (image.shape[1], image.shape[0]), True)
        create.write(image)
        key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
        #TIMER = int(3)
        #prev = time.time()
        cur = time.time()
        if cur-prev >= 15:
            break
        if key == ord("q"):
        
          break
      
    # do a bit of cleanup
    cv2.destroyAllWindows()



def final_display(line1,counter):
    total_count = db.fetch_only_count(line1)
    root=Tk()
    root.title("Output")
    root.geometry("1920x1080")
    w=Label(root,text="SRN : " + line1 +"\n"+"Current Squats = "+str(counter)+"\n"+"Total Squats = "+str(total_count),font=("Courier", 30))
    w.pack()
    w.place(relx=0.5,rely=0.5,anchor=CENTER)
    root.after(3000,lambda:root.destroy())
    root.mainloop()


def start():
    while (TRUE):
        #print("begin of main while")
        Flag =True
        global try_again_counter
        try_again_counter =0
        #cap = cv2.VideoCapture(0)
        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils
        finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
        thumb_Coord = (4,2)
        count = 0
        hand=False
        hand_again=False
        while (Flag):
            #cv2.imshow("PESU", img)
            #cv2.waitKey(0)
            #Picture.show()
            hand=False
            hand_again=False
            success, image = cap.read()
            RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(RGB_image)
            multiLandMarks = results.multi_hand_landmarks
            if multiLandMarks:
                handList = []
                for handLms in multiLandMarks:
                    mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                    for idx, lm in enumerate(handLms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        handList.append((cx, cy))
                    for point in handList:
                        cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
                        upCount = 0
                        for coordinate in finger_Coord:
                            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                                upCount += 1
                        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                            upCount += 1
                        if upCount==2:
                            hand =True
                            print("Hand first time read")
                            print(time.time())
            time.sleep(2)
            success, image = cap.read()
            imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(imageRGB)
            if multiLandMarks:
                handList = []
                for handLms in multiLandMarks:
                    mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                    for idx, lm in enumerate(handLms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        handList.append((cx, cy))
                    for point in handList:
                        cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
                        upCount = 0
                        for coordinate in finger_Coord:
                            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                                upCount += 1
                        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                            upCount += 1
                        if upCount==2:        
                            hand_again =True
                            print("Hand second time read")
                            print(time.time())
                        #cv2.destroyAllWindows()
            if ((hand==True) & (hand_again==True)):
                OCR()
                time.sleep(3)
                success, image = cap.read()
                squat_counter(line1)
                print(counter)
                print(line1)
                db.initialise_data_base('PESUfitness')
                if (db.fetch_only_student(line1)):
                    db.increment_number_of_squats(line1,counter)
                else:
                    db.create_new_student(line1)
                    db.increment_number_of_squats(line1,counter)
                #total_count = db.fetch_only_count(line1)
                print("end of flag while")
                final_display(line1,counter)
                print("end of flag while")
                Flag = False
        print("End of main while")
    
start()
