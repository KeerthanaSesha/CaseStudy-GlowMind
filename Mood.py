def log_mood():
    mood = input("How are you feeling? (happy/sad/neutral): ")

    try:
        with open("data/mood.txt", "a") as file:
            file.write(mood + "\n")
        print("Mood saved successfully!")
    except:
        print("Error saving mood.")
