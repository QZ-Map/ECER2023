import cv2

# Capturing Video from Webcam
cap = cv2.VideoCapture(0)
#0 is your camera, if you have multiple camera, you need to enter their id
while(True):
    # Capturing frame-by-frame
    _, frame = cap.read()
    cv2.imshow('Frame',frame)
    # When user presses q -> quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Camera must be released
cap.release()
