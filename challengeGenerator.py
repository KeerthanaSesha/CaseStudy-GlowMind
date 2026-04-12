import random

challenges = [
    "Drink 2 liters of water today 💧",
    "Walk 5000 steps 🚶",
    "Stay off social media for 2 hours 📵",
    "Write 3 things you're grateful for 🙏",
    "Do 10 minutes of stretching 🧘",
    "Compliment someone today 😊"
    "Finish that project."
    "Finish a penting task."
    "Make a sketch."
    "Write out what you're feeling in the form of a poem."
    "Read a new book."
]

def get_challenge():
    print("\n🎯 Today's Challenge:")
    print(random.choice(challenges))
