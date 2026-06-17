import cv2
from datetime import datetime
from pathlib import Path

#Create Folders
folders = [
    "data/outside",
    "data/food",
    "data/play",
    "data/rest"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

print("Folders Created")



#Working with the Webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Webcam Feed", frame)
    #image = cv2.resize(frame, 224, 224)


    key = cv2.waitKey(1)
    if key in [27, ord('q')]:
        print("Quit Feed")
        break
    if key in [ord('s')]:
        now = datetime.now()
        stamp = f"{now:%Y%m%d_%H%M%S_%f}"
        cv2.imwrite(f"data/play/test_image{stamp}.jpg", frame)
        print(f"Saved {stamp}")
        
    
    

camera.release()
cv2.destroyAllWindows()
