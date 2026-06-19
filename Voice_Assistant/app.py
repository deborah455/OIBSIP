import datetime
import webbrowser

print("=== PYTHON ASSISTANT ===")
print("Commands: time, date, google, help, exit")

while True:
    command = input("\nEnter command: ").lower().strip()

    if command == "time":
        print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif command == "date":
        print("Today's Date:", datetime.datetime.now().strftime("%Y-%m-%d"))

    elif command == "google":
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif command == "help":
        print("Available commands:")
        print("- time")
        print("- date")
        print("- google")
        print("- exit")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Command not recognized.")
