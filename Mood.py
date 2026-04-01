MOODS = ["happy", "sad", "neutral", "angry", "stressed", "excited"]

def get_advice(mood, intensity):
    if mood == "stressed":
        if intensity <= 2:
            return "Drink some water, calm down, breathe. You will be alright 💙"
        elif intensity <= 4:
            return "Take a short break, listen to music, and relax a bit 🎧"
        else:
            return "You seem very stressed. Try deep breathing or talk to someone you trust 🤍"

    elif mood == "sad":
        if intensity <= 2:
            return "It's okay to feel low sometimes. Try doing something you enjoy 🌸"
        elif intensity <= 4:
            return "Maybe talk to a friend or write your thoughts down 📝"
        else:
            return "You're not alone. Please consider reaching out to someone you trust 💙"

    elif mood == "happy":
        return "That's amazing! Keep spreading the positivity ✨"

    elif mood == "angry":
        return "Take a deep breath. Give yourself some time before reacting 🔥➡️😌"

    elif mood == "excited":
        return "Love the energy! Use it to do something productive 🚀"

    elif mood == "neutral":
        return "A calm day is still a good day. Keep going 👍"

    return "Take care of yourself 💫"


def log_mood():
    print("\nAvailable moods:", ", ".join(MOODS))

    mood = input("Enter your mood: ").lower()

    if mood not in MOODS:
        print("Invalid mood.")
        return

    try:
        intensity = int(input("Enter intensity (1-5): "))
        if intensity < 1 or intensity > 5:
            print("Intensity must be between 1 and 5.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    print("\n🧠 Glow Mind says:")
    print(get_advice(mood, intensity))
