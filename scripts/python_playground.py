translations = {
    "outside": "I want to go outside",
    "food": "I'm hungry",
    "play": "I want to play",
    "rest": "I want to rest"
}

def dog_translate(intent):
    if intent in translations:
        return translations[intent]
    else:
        return "Screw you human"

user_input = input("Enter dog intent: ").lower()

print(dog_translate(user_input))

