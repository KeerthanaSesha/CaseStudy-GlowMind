def write_journal():
    entry = input("Write your journal entry: ")

    try:
        with open("data/journal.txt", "a") as file:
            file.write(entry + "\n---\n")
        print("Journal saved!")
    except:
        print("Error saving journal.")
