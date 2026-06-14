intent = input("Enter dog intent: ")
with open("docs/latest_intent.txt", "w") as file:
    file.write(intent)


print("Intent saved", intent)