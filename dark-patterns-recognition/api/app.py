from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import easyocr
import cv2
from matplotlib import pyplot as plt


presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []
        print(request.get_json())
        data = request.get_json().get('tokens')

        for token in data:
            result = presence_classifier.predict(presence_vect.transform([token]))
            if 'Dark' in result:
                cat = category_classifier.predict(category_vect.transform([token]))
                output.append(cat[0])
            else:
                output.append(result[0])

        dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']
        for d in dark:
            print(d)
        print()
        print(len(dark))

        message = { 'result': output }
        print(message)

        return jsonify(message)
@app.route('/ocr',methods=['POST'])
def ocr():
    save_path='screenshot.png'
    data = request.get_json()  # Corrected line
    url = data.get('url')    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        driver.implicitly_wait(5)
        driver.save_screenshot(save_path)
        print("screenshot successful")
    finally:
        driver.quit()
    font = cv2.FONT_HERSHEY_SIMPLEX
    image_path="screenshot.png"
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    img = cv2.imread(image_path)
    Dresult=[]
    for detection in result:
        text = detection[1] 
        if detection[2] > 0.5:
            Dresult = presence_classifier.predict(presence_vect.transform([text]))
        
            if Dresult[0] == "Dark":
                cat = category_classifier.predict(category_vect.transform([text]))
                Dresult[0]=cat[0]
    
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
    
           
               
           
        # Check if coordinates are within bounds
        if all(0 <= coord <= max_dim for coord in top_left + bottom_right for max_dim in img.shape[:2]):
            annote = Dresult[0]
            
            # Draw rectangle
            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 1)
            
            # Draw text
            img = cv2.putText(img, annote, top_left, font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

    
    
    plt.imshow(img)
    plt.show()

    return "screenshot downloaded"

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
