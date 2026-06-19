import datetime
import webbrowser
import wikipedia


def show_time():
    print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))


def show_date():
    print("Today's Date:", datetime.datetime.now().strftime("%Y-%m-%d"))


def open_google():
    print("Opening Google...")
    webbrowser.open("https://www.google.com")


def search_topic(topic):
    try:
        result = wikipedia.summary(topic, sentences=2)
        print("\nSearch Result:")
        print(result)
    except Exception:
        print("Could not find information about that topic.")


def calculate(expression):
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception:
        print("Invalid expression.")


def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved.")


def show_help():
    print("""
Available Commands
------------------
time
date
google
search <topic>
calc <expression>
note <text>
help
exit
""")


print("=== PERSONAL PRODUCTIVITY ASSISTANT ===")
print("Type 'help' to see available commands.")

while True:
    command = input("\nEnter command: ").strip()

    if command.lower() == "time":
        show_time()

    elif command.lower() == "date":
        show_date()

    elif command.lower() == "google":
        open_google()

    elif command.lower().startswith("search "):
        topic = command[7:]
        search_topic(topic)

    elif command.lower().startswith("calc "):
        expression = command[5:]
        calculate(expression)

    elif command.lower().startswith("note "):
        note = command[5:]
        save_note(note)

    elif command.lower() == "help":
        show_help()

    elif command.lower() == "exit":
        print("Goodbye!")
        break

    else:
        print("Command not recognized. Type 'help'.")
