"""
Regestration Page 📃
"""
import re
import json

#saving data to json file
def saveData(user_data):
    try:
        with open("data.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(user_data)

    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

#Validation of first name 
def firstName() :
    try :
        fname = input("Enter your first name : ")
        if fname.isdigit() :
            raise Exception ("First Name must be string ⛔️")
        return fname
    except ValueError as ve:
        print(f"Error : {ve}")

# Validation of last name
def lastName() :
    try :
        lname = input("Enter your last name : ")
        if lname.isdigit() :
            raise Exception ("Last Name must be string ⛔️ ")
        return lname
    except ValueError as ve:
        print(f"Error : {ve}")

# Validation of email 
def emailValidation () :
        email = input("Enter your email : ")
        validEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        try:
            with open("data.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        for user in users:
            if user["email"] == email:
                raise Exception ("Email already exists. Please use a different email.")

        while not re.match(validEmail, email):
            print("You entered a wrong value ⛔️")
            email = input("Enter your email again: ")
        
        return email
            
# Validation of password 
def passwordValidation () :
    global password
    password = input("Enter a password : ")
    validPassword = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    while True :
        if re.match(validPassword , password) :
            return password
        else :
            print("password are: Should have at least one number , Should have at least one uppercase and one lowercase character , Should have at least one special symbol , Should be between 6 to 20 characters long.")
            password = input("Please try again 😩 ")
            
# Conformation of password
def confirmPassword(password):
    password_confirmation = input("Please confirm your password: ")
    while password_confirmation != password:
        print("Passwords do not match.. 🤨")
        password_confirmation = input("Please confirm your password: ")
    print("Passwords match ✅")
    return True


#Validation of phone 
def phoneValidation():
    validPhone = r"^01[0125]\d{8}$"
    while True:
        phone = input("Enter your phone number: ")
        if not phone.isdigit():
            print("Phone must be numeric digits only 🤖")
        elif not re.match(validPhone, phone):
            print("Phone must contain 11 digits and match the required format. Try Again ..")
        else:
            print("Saving the data..🧾")
            return phone

 
#Regestration
def registration():
    fname = firstName()
    lname = lastName()
    email = emailValidation()
    password = passwordValidation()
    confirmPassword(password)
    phone = phoneValidation()

    user_data = {
        "first_name": fname,
        "last_name": lname,
        "email": email,
        "password": password,
        "phone": phone,
    }

    saveData(user_data)
    print("Data Saved Successfully. ✅")