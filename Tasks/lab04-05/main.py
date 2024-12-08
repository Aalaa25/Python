import emoji
import regestrationPage
import loginPage

print(emoji.emojize("Welcome!!\nIt's very nice to see you again.. :red_heart:", variant="emoji_type"))
while True:
    try:
        choose = int(input("If you want to create a new account press 1, or if you already have an account press 2: "))
        
        if choose == 1:
            print("___Registration___")
            print("Please fill out this form ..")
            regestrationPage.registration()
            break

        elif choose == 2:
            print("___Login___")
            email = loginPage.login()
            break

        else:
            print("You entered a wrong value..❌ Please choose 1 or 2.")
    except ValueError:
        print("You must choose 1 or 2 .. 🚫 Please enter a valid number.")
