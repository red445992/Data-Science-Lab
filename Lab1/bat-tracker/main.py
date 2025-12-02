from database import load_criminals, save_criminals
from models import Criminal


def display_menu():
    print("\n=== 🦇 BAT TRACKER MENU ===")
    print("1. Add Criminal")
    print("2. Update Criminal")
    print("3. Search by Name")
    print("4. Search by Threat Level")
    print("5. Sort by Threat (High → Low)")
    print("6. View All Criminals")
    print("7. Exit")


def add_criminal(criminals):
    name = input("Enter name: ").strip()
    threat = int(input("Threat level (1–5): "))
    last_seen = input("Last seen location: ").strip()

    criminal = Criminal(name, threat, last_seen)
    criminals.append(criminal)

    print(f"🆕 Added {name} to the database!")


def update_criminal(criminals):
    name = input("Enter the name of the criminal to update: ").strip()
    for c in criminals:
        if c.name.lower() == name.lower():
            print("Found! What do you want to update?")
            print("1. Threat level")
            print("2. Last seen location")

            choice = input("Choose: ")

            if choice == "1":
                c.threat = int(input("New threat level: "))
                print("Threat updated!")
            elif choice == "2":
                c.last_seen = input("New last seen location: ")
                print("Location updated!")
            else:
                print("Invalid choice!")

            return

    print("❌ Criminal not found.")


def search_by_name(criminals):
    name = input("Enter name to search: ")
    for c in criminals:
        if c.name.lower() == name.lower():
            print(f"\nFound:")
            print(f"Name: {c.name}")
            print(f"Threat: {c.threat}")
            print(f"Last seen: {c.last_seen}")
            return

    print("❌ No match found.")


def search_by_threat(criminals):
    threat = int(input("Show criminals with threat level ≥ "))
    results = [c for c in criminals if c.threat >= threat]

    if not results:
        print("No criminals match that threat level.")
        return

    print("\nMatches:")
    for c in results:
        print(f"- {c.name} (Threat {c.threat}) — Last seen: {c.last_seen}")


def sort_by_threat(criminals):
    sorted_list = sorted(criminals, key=lambda c: c.threat, reverse=True)

    print("\nSorted (High → Low):")
    for c in sorted_list:
        print(f"- {c.name}: Threat {c.threat}")


def view_all(criminals):
    if not criminals:
        print("Database is empty.")
        return

    print("\n=== Current Criminal Profiles ===")
    for c in criminals:
        print(f"- {c.name} | Threat: {c.threat} | Last seen: {c.last_seen}")


def main():
    criminals = load_criminals()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_criminal(criminals)
        elif choice == "2":
            update_criminal(criminals)
        elif choice == "3":
            search_by_name(criminals)
        elif choice == "4":
            search_by_threat(criminals)
        elif choice == "5":
            sort_by_threat(criminals)
        elif choice == "6":
            view_all(criminals)
        elif choice == "7":
            save_criminals(criminals)
            print("💾 Saved. Exiting Bat-Tracker...")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
