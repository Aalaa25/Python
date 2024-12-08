import json
import createProjectPage

def login():
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    try:
        with open("data.json", "r") as file:
            users = json.load(file)
        
        if isinstance(users, list):
            for user in users:
                if isinstance(user, dict) and user.get("email") and user.get("password"):
                    if user["email"].strip().lower() == email.lower() and user["password"] == password:
                        print("Login successful! ✅")
                        
                        while True:
                            try:
                                choice = int(input("If you want to create a new project, press 3: "))
                                if choice == 3:
                                    createProjectPage.createProject(email)
                                    break
                                else:
                                    print("Invalid choice. Please press 3 if you want to create a project.")
                            except ValueError:
                                print("Please enter a valid number.")
                        
                        return email
        print("Invalid email or password.")
    except FileNotFoundError:
        print("File not found. Please initialize the data file first.")
    except json.JSONDecodeError:
        print("Error reading JSON data. The file may be corrupted.")
    
    return None
