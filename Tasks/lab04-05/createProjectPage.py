import json
from datetime import datetime
import showingProjectPage

def titleValidation():
    print("Creating new project..🤖")
    while True:
        title = input("Enter the title of the project: ")
        if title.isdigit() or len(title) == 0:
            print("Title must be a string and not empty ⛔️")
        else:
            return title

def detailsValidation():
    while True:
        details = input("Enter the details of the project: ")
        if details.isdigit() or len(details) == 0:
            print("Details must be a string and not empty ⛔️")
        else:
            return details

def targetValidation():
    while True:
        target = input("Enter the target of the project: ")
        if not target.isdigit():
            print("Target must be an integer ⛔️")
        else:
            return int(target)

def dateValidation():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            validDate = datetime.strptime(date, "%Y-%m-%d")
            return validDate
        except ValueError:
            print("Invalid date format 🚫. Please use YYYY-MM-DD.")
            input("Try Again...😔")

def createProject(email):
    title = titleValidation()
    details = detailsValidation()
    target = targetValidation()
    date = dateValidation()

    new_project = {
        "name": title,
        "description": details,
        "target": target,
        "date": date.strftime("%Y-%m-%d")
    }

    try:
        with open("data.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["email"] == email:
                if "projects" not in user:
                    user["projects"] = []
                user["projects"].append(new_project)
                
                with open("data.json", "w") as file:
                    json.dump(users, file, indent=4)
                
                print(f"Project '{title}' has been created successfully! ✅")

                while True:
                    try:
                        choice = int(input("If you want to show your projects, press 4: "))
                        if choice == 4:
                            showingProjectPage.showProjects(email)
                            break
                        else:
                            print("Invalid choice. Please press 4 to show your projects.")
                    except ValueError:
                        print("Please enter a valid number.")
                return

        print("User not found. Project creation failed.")
    except FileNotFoundError:
        print("File not found 😩")
