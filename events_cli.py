import json
import os
import platform
from datetime import datetime

EVENTS_FILE = "events.json"
DATE_FORMAT = "%d/%m/%Y"

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def load_events():
    if not os.path.exists(EVENTS_FILE):
        return []
    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_events(events):
    def event_date(event):
        try:
            return datetime.strptime(event["Date"], DATE_FORMAT)
        except Exception:
            return datetime.max
    events.sort(key=event_date)
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

def input_valid_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, DATE_FORMAT)
            return date_str
        except ValueError:
            print(f"Invalid date format. Please use DD/MM/YYYY.")

def add_event():
    clear_screen()
    print("Add a new event")
    name = input("Event Name: ").strip()
    date = input_valid_date("Date (DD/MM/YYYY): ")
    place = input("Place: ").strip()
    event_type = input("Type: ").strip()
    description = input("Description: ").strip()
    event = {
        "Event Name": name,
        "Date": date,
        "Place": place,
        "Type": event_type,
        "Description": description
    }
    events = load_events()
    events.append(event)
    save_events(events)
    print("Event added successfully!")

def list_events():
    clear_screen()
    events = load_events()
    if not events:
        print("No events found.")
    else:
        for idx, event in enumerate(events, 1):
            print(f"{idx}. {event['Event Name']} ({event['Date']}) at {event['Place']} [{event['Type']}]: {event['Description']}")

def remove_event():
    clear_screen()
    events = load_events()
    if not events:
        print("No events to remove.")
        return
    for idx, event in enumerate(events, 1):
        print(f"{idx}. {event['Event Name']} ({event['Date']}) at {event['Place']} [{event['Type']}]: {event['Description']}")
    try:
        idx = int(input("\nEnter the number of the event to remove: ").strip())
        if 1 <= idx <= len(events):
            removed = events.pop(idx - 1)
            save_events(events)
            print(f"Removed event: {removed['Event Name']}")
        else:
            print("Invalid event number.")
    except ValueError:
        print("Please enter a valid number.")

def edit_event():
    clear_screen()
    events = load_events()
    if not events:
        print("No events to edit.")
        return
    for idx, event in enumerate(events, 1):
        print(f"{idx}. {event['Event Name']} ({event['Date']}) at {event['Place']} [{event['Type']}]: {event['Description']}")
    try:
        idx = int(input("\nEnter the number of the event to edit: ").strip())
        if 1 <= idx <= len(events):
            event = events[idx - 1]
            print("\nLeave blank to keep current value.")
            name = input(f"Event Name [{event['Event Name']}]: ").strip()
            date = input(f"Date [{event['Date']}]: ").strip()
            if date:
                while True:
                    try:
                        datetime.strptime(date, DATE_FORMAT)
                        break
                    except ValueError:
                        print("Invalid date format. Please use DD/MM/YYYY.")
                        date = input(f"Date [{event['Date']}]: ").strip()
            place = input(f"Place [{event['Place']}]: ").strip()
            event_type = input(f"Type [{event['Type']}]: ").strip()
            description = input(f"Description [{event['Description']}]: ").strip()
            if name:
                event['Event Name'] = name
            if date:
                event['Date'] = date
            if place:
                event['Place'] = place
            if event_type:
                event['Type'] = event_type
            if description:
                event['Description'] = description
            save_events(events)
            print("Event updated successfully!")
        else:
            print("Invalid event number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        clear_screen()
        print("Event Manager")
        print("1. Add new event")
        print("2. List events")
        print("3. Remove event")
        print("4. Edit event")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_event()
            input("\nPress Enter to continue...")
        elif choice == "2":
            list_events()
            input("\nPress Enter to continue...")
        elif choice == "3":
            remove_event()
            input("\nPress Enter to continue...")
        elif choice == "4":
            edit_event()
            input("\nPress Enter to continue...")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()