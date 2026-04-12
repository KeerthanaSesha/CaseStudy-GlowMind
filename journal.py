import datetime

def write_journal():
    print("\n📝 Write your journal entry (type 'END' on a new line to finish):\n")

    lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    if not lines:
        print("Empty entry. Nothing saved.")
        return

    entry = "\n".join(lines)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_entry = f"\n--- {timestamp} ---\n{entry}\n"

    try:
        with open("data/journal.txt", "a") as file:
            file.write(formatted_entry)
        print("✅ Journal entry saved!")
    except Exception as e:
        print("Error saving journal:", e)


def view_journal():
    print("\n📖 Your Journal Entries:\n")

    try:
        with open("data/journal.txt", "r") as file:
            content = file.read()

            if not content.strip():
                print("No journal entries found.")
            else:
                print(content)

    except FileNotFoundError:
        print("No journal file found yet.")
    except Exception as e:
        print("Error reading journal:", e)


def search_journal():
    keyword = input("Enter a keyword to search: ").lower()

    try:
        with open("data/journal.txt", "r") as file:
            entries = file.read().split("---")

            found = False
            for entry in entries:
                if keyword in entry.lower():
                    print("\n🔍 Match found:")
                    print("---" + entry)
                    found = True

            if not found:
                print("No matching entries found.")

    except FileNotFoundError:
        print("No journal file found yet.")
    except Exception as e:
        print("Error searching journal:", e)
