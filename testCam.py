import sys
import cv2
import cv2.data
import numpy
#cascade = cv2.Load('haarcascade_frontalface_alt.xml')

face_cascade = cv2.CascadeClassifier(r'/tmp/untitled3/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
profil_face_cascad=cv2.CascadeClassifier(r'/tmp/untitled3/venv/lib/python3.6/site-packages/cv2/data/haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier(r'/tmp/untitled3/venv/lib/python3.6/site-packages/cv2/data/haarcascade_smile.xml')


if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    while 1:
        ret,frame =cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces_prof=profil_face_cascad.detectMultiScale(gray, 1.3,5)
        for (x, y, w, h) in faces:
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]


        #    for (ex, ey, ew, eh) in eyes:
         #       cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)



       # frame = numpy.asarray(detect(frame))
        cv2.imshow("features", frame)
        cv2.imshow('fdf',gray)
        if cv2.waitKey(10) == 0x1b: # ESC
            print ('ESC pressed. Exiting ...')
            break