from joblib import load
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')
font = cv2.FONT_HERSHEY_SIMPLEX
image_path="dp2.jpg"
reader = easyocr.Reader(['en'])
result = reader.readtext(image_path)

img = cv2.imread(image_path)

for detection in result:
    text = detection[1] 
    if detection[2] > 0.5:
        Dresult = presence_classifier.predict(presence_vect.transform([text]))
        if Dresult[0] == "Dark":
            cat = category_classifier.predict(category_vect.transform([text]))
            Dresult[0]=cat[0]
        print(text,Dresult[0])
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])

        # Check if coordinates are within bounds
        if all(0 <= coord <= max_dim for coord in top_left + bottom_right for max_dim in img.shape[:2]):
            annote = Dresult[0]
            
            # Draw rectangle
            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 1)
            
            # Draw text
            img = cv2.putText(img, annote, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

    
    
plt.imshow(img)
plt.show()
