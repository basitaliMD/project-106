import cv2

#create our body classifier
body_Classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
     #CascadeClassifier needs grayScale
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     bodies = body_Classifier.detectMultiScale(gray, 1.2, 3)
      
     for (x, y, w, h) in bodies:
          cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
          cv2.imshow("walking.avi", gray)
          