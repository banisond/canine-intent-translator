from translator import translate
import pyttsx3

def menu():
    print("1. Outside")
    print("2. Food")
    print("3. Play")
    print("4. Rest")

while True:
    menu()
    choice = input("Select an option 1-4: ")

    if choice == "1":
        intent = "outside"
        break
    if choice == "2":
        intent = "food"
        break
    if choice == "3":
        intent = "play"
        break
    if choice == "4":
        intent = "rest"
        break
    else:
        print("Error invalid selection")
        break


engine = pyttsx3.init()

message = translate(intent)


engine.say(message)
engine.runAndWait()

#fake confidence scores
prediction = {
    "intent" : "outside",
    "confidence" : "82%"
}

with open("docs/predictions.txt", "a") as file:
    file.write("\n" + intent)


print ("Predicted intent:", prediction.get("intent"))
print ("Predicted confidence:", prediction.get("confidence"))

print (message)

# python3 scripts/main.py