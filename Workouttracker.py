def log_workout():
    workout = input("Enter workout (Running/Gym/Yoga): ")
    duration = input("Enter duration (minutes): ")

    try:
        with open("data/workout.txt", "a") as file:
            file.write(workout + "," + duration + "\n")
        print("✅ Workout saved!")
    except:
        print("Error saving workout.")


def view_workouts():
    print("\n📖 Workout History:\n")

    try:
        with open("data/workout.txt", "r") as file:
            data = file.read()

            if not data:
                print("No workouts found.")
            else:
                print(data)

    except:
        print("No workout file found.")
