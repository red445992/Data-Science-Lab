from database import load_criminals, save_criminals, load_missions, save_missions
from models import criminal, Mission

def display_menu():
    print("\n=== BAT ASSISTANT MENU ===")
    print("1. Add Criminal")
    print("2. View All Criminals")
    print("3. Add Mission")
    print("4. View All Missions")
    print("5. Exit")

def add_criminal(criminals):
    name = input("Enter name: ").strip()
    threat = int(input("Threat level (1–5): "))
    last_seen = input("Last seen location: ").strip()

    new_criminal = criminal(name, threat, last_seen)
    criminals.append(new_criminal)

    print(f" Added {name} to the database!")

def view_all_criminals(criminals):
    if not criminals:
        print("No criminals in the database.")
        return

    print("\n=== All Criminals ===")
    for c in criminals:
        print(f"Name: {c.name}, Threat: {c.threat}, Last seen: {c.last_seen}")

def add_mission(missions, criminals):
    description = input("Enter mission description: ").strip()
    target_name = input("Enter target criminal name: ").strip()
    piority = input("Enter mission priority (Low/Medium/High): ").strip()
    status = input("Enter mission status (Pending/In Progress/Completed): ").strip()

    target_criminal = next((c for c in criminals if c.name.lower() == target_name.lower()), None)
    if not target_criminal:
        print(" Criminal not found. Mission not added.")
        return

    new_mission = Mission(description, target_criminal.name, piority, status)
    missions.append(new_mission)

    print(f" Added mission targeting {target_criminal.name}.")

def view_all_missions(missions):
    if not missions:
        print("No missions in the database.")
        return

    print("\n=== All Missions ===")
    for m in missions:
        print(f"Description: {m.description}, Target: {m.target_criminal}, Priority: {m.piority}, Status: {m.status}")


def main():
    criminals = load_criminals()
    missions = load_missions()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_criminal(criminals)
            save_criminals(criminals)
        elif choice == "2":
            view_all_criminals(criminals)
        elif choice == "3":
            add_mission(missions, criminals)
            save_missions(missions)
        elif choice == "4":
            view_all_missions(missions)
        elif choice == "5":
            print("Exiting Bat Assistant. Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()