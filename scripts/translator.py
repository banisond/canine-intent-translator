translations = {
    "outside" : "I want to go outside",
    "food" : "Can you feed me?",
    "play" : "Play with me pleaseeee",
    "rest" : "I need to rest"
}

def translate (intent):
    return translations.get(
        intent,
        "I don't understand"
    )