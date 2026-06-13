translations = {
    "outside": "I want to go outside;",
    "food": "I'm hungry",
    "play": "I want to play",
    "rest": "I want to rest"
}

intent = input("Enter dog intent:  ").lower()

if intent in translations:
    print(translations[intent])
else:
    print("Screw you human")