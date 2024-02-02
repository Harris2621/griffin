import cv2
from easyocr import Reader

# Function to perform OCR on the given image
def perform_ocr(image, reader):
    results = reader.readtext(image)
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, f'{text} ({prob:.2f})', (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return image

# Initialize the EasyOCR reader
reader = Reader(['en'])

# Open a video capture object (you can change the argument to 0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Perform OCR on the frame
    result_frame = perform_ocr(frame, reader)

    # Display the resulting frame
    cv2.imshow('Live OCR', result_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
