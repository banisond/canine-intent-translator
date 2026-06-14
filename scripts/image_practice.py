'''
from pathlib import Path

folders = [
    "data/outside",
    "data/food",
    "data/play",
    "data/rest"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

print("Folders Created")
'''
'''
from PIL import Image

image = Image.open("data/test_dog.jpeg")

resized= image.resize((224, 224))
resized.save("data/resized_dog.jpeg")

print(image.size)
print(resized.size)
print("Saved resized image")
'''


from pathlib import Path
from PIL import Image

outside_folder = Path("data/outside")

images = list(outside_folder.glob("*.jpg"))
print("Found ",len(images)," images.")

for image_path in outside_folder.glob("*.jpg"):

    image = Image.open(image_path)

    resized = image.resize((224, 224))

    resized.save(image_path)

    print("Processed:", image_path.name)


