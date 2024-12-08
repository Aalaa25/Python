import json
from datetime import datetime

def showProjects(email):
    try:
        with open("data.json", "r") as file:
            users = json.load(file)
        
        for user in users:
            if user["email"] == email:
                if "projects" in user and user["projects"]:
                    print("Your Projects: 📂")
                    for i, project in enumerate(user["projects"], 1):
                        print(f"{i}. Title: {project['name']}")
                        print(f"   Description: {project['description']}")
                        print(f"   Target: {project['target']}")
                        print(f"   Date: {project['date']}")
                        
                    while True:
                        try:
                            action = int(input(
                                "Choose an option:\n"
                                "1. Edit a project\n"
                                "2. Delete a project\n"
                                "3. Search a project by date\n"
                                "0. Exit\n"
                                "Your choice: "
                            ))

                            if action == 1:
                                editProject(user, users, email)
                            elif action == 2:
                                deleteProject(user, users, email)
                            elif action == 3:
                                searchProjectByDate(user)
                            elif action == 0:
                                print("Exiting project management.")
                                return
                            else:
                                print("Invalid choice. Please choose 1, 2, 3, or 0.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                else:
                    print("There are no projects for you yet. You can create one if you want!")
                    return None
        print("User not found.")
        return None
    except FileNotFoundError:
        print("File not found. Please initialize the data file first.")
        return None
    except json.JSONDecodeError:
        print("Error reading JSON data. The file may be corrupted.")
        return None

def editProject(user, users, email):
    try:
        project_number = int(input("Enter the number of the project you want to edit: "))
        if 1 <= project_number <= len(user["projects"]):
            project_to_edit = user["projects"][project_number - 1]
            
            new_title = input(f"Enter new title (current: {project_to_edit['name']}): ")
            new_description = input(f"Enter new description (current: {project_to_edit['description']}): ")
            new_target = input(f"Enter new target (current: {project_to_edit['target']}): ")
            new_date = input(f"Enter new date (current: {project_to_edit['date']}): ")
            
            # Directly update fields without checks
            project_to_edit["name"] = new_title
            project_to_edit["description"] = new_description
            if new_target.isdigit():  # Ensure target is valid numeric value
                project_to_edit["target"] = int(new_target)
            project_to_edit["date"] = new_date
            
            with open("data.json", "w") as file:
                json.dump(users, file, indent=4)
            
            print("Project updated successfully! ✅")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def deleteProject(user, users, email):
    try:
        project_number = int(input("Enter the number of the project you want to delete: "))
        if 1 <= project_number <= len(user["projects"]):
            projectDelete = user["projects"].pop(project_number - 1)
            
            with open("data.json", "w") as file:
                json.dump(users, file, indent=4)
            
            print(f"Project '{projectDelete['name']}' deleted successfully! ✅")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def searchProjectByDate(user):
    try:
        search_date = input("Enter the date to search for projects (YYYY-MM-DD): ")
        try:
            valid_date = datetime.strptime(search_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        found_projects = [project for project in user["projects"] if project["date"] == valid_date]
        
        if found_projects:
            print(f"Projects on {valid_date}: 📅")
            for i, project in enumerate(found_projects, 1):
                print(f"{i}. Title: {project['name']}")
                print(f"   Description: {project['description']}")
                print(f"   Target: {project['target']}")
                print(f"   Date: {project['date']}")
        else:
            print(f"No projects found on {valid_date}.")
    except KeyError:
        print("No projects available for searching.")
