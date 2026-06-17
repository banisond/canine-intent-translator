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

#Choose which folder to save to
def menu():
    print("1. Outside")
    print("2. Food")
    print("3. Play")
    print("4. Rest")


def choose():
    while True:
        menu()
        choice = input("Select an option 1-4: ")
        if choice == "1":
            return "outside"
            break
        if choice == "2":
            return "food"
            break
        if choice == "3":
            return "play"
            break
        if choice == "4":
            return "rest"
            break
        else:
            print("Error invalid selection")
            





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
        cv2.imwrite(f"data/{choose()}/test_image{stamp}.jpg", frame)
        print(f"Saved {stamp}")
        
    
    

camera.release()
cv2.destroyAllWindows()

# python3 scripts/collect_dataset.py
