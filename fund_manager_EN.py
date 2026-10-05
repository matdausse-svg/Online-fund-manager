# os is used to check file information (new list with the creator's funds)
# json library used to work with files
import os
import json

def verify_int(x):
    # Checks that x is a number
    verified = 0
    while verified == 0:
        if x.isalpha():
            # checks if x is a letter
            x = input("error, please enter a number  ")
        else:
            verified = 1
            x = (int(x))
            return x

def main_menu():
    # Main menu function
    print("""
    Hello, welcome to the online fund manager, what would you like to do?
    """)
    x = input('''
    If you want to sign up type       :  1
    If you want to log in type        :  2
    If you are a guest and want to contribute to a fund type : 3
    Exit the site type                :  4
    ''')
    x = verify_int(x)
    while x > 4 or x < 1:
        print(
            "Please select a number between 1 and 4 corresponding to your request."
        )
        x = input("""
        If you want to sign up type       :  1
        If you want to log in type        :  2
        If you are a guest and want to contribute to a fund type : 3
        Exit the site type                :  4
        """)
        x = verify_int(x)
    return x

def registration(user_list):
    # Sign-up function
    print("Registration: ")
    new_user = {
        "email": 0,
        "password": 0,
        "last_name": 0,
        "first_name": 0,
        "gender": 0,
        "age": 0,
        "nationality": 0
    }
    em = input("""
    What is your email?
    """)
    ver = check_email_exists(em, user_list)
    if ver == 1:
        pas = input("""
        What is your password?
        """)
        ln = input("""
        What is your last name?
        """)
        fn = input("""
        What is your first name?
        """)
        gd = input("""
        Are you a woman, a man, or non-binary?
        """)
        while gd != 'man' and gd != 'woman' and gd != "non-binary":
            print("You must answer the question with woman, man, or non-binary.")
            gd = input("""
            Are you a woman, a man, or non-binary?
            """)
            print("You are ", gd)
        nat = input("""What is your nationality?
        """)
        x = input("""
        How old are you?
        """)
        verify_int(x)
        new_user["email"] = em
        new_user["password"] = pas
        new_user["last_name"] = ln
        new_user["first_name"] = fn
        new_user["gender"] = gd
        new_user["age"] = x
        new_user["nationality"] = nat
        new_user["comment"] = 0

        # Add the new_user dict to the list
        user_list.append(new_user)

def check_email_exists(em, user_list):
    # Checks the email during registration
    for i in range(len(user_list)):
        v = user_list[i]["email"]
        if v == em:
            print("We already have an account for this email address")
            return 0
    return 1

def check_login(user_list):
    # Login verification function
    print("Login: ")
    em1 = 1
    pas = 1
    ve = 0
    we = 0
    done = 0
    while done == 0:
        found = 0
        em1 = input("""
        What is your email address?
        """)
        pas = input("""
        What is your password?
        """)
        for i in range(len(user_list)):
            ve = user_list[i]["email"]
            we = user_list[i]["password"]
            if ve == em1 and we == pas:
                print("You are logged in")
                found = 1
                done = 1
                break
        if found == 0:
            print("The password or email address is not recognized")
    return em1

def fund_menu():
    # Fund management menu function
    x = input("""
    If you want to create a fund type            :  1
    If you want to access the fund comments type  :  2
    If you want to cancel a fund type             :  3
    If you want to delete a fund type             :  4
    If you want to edit your profile comment type :  5
    Exit the site type                            :  6
    """)
    x = verify_int(x)
    while x > 6 or x < 1:
        print(
            "Please select a number between 1 and 4 corresponding to your request."
        )
        x = input("""
        If you want to create a fund type            :  1
        If you want to access the fund comments type  :  2
        If you want to cancel a fund type             :  3
        If you want to delete a fund type             :  4
        If you want to edit your profile comment type :  5
        Exit the site type                            :  6
        """)
        x = verify_int(x)
    return x

def create_fund(user_list, fund_list, email):
    # Fund creation function
    fund = {
        "creator_email": 0,
        "fund_name": 0,
        "event_date": 0,
        "event_type": 0,
        "gift": 0,
        "participation_type": 0,
        "identification_type": 0,
        "participants": 0,
        "amount": 0
    }
    # retrieves the creator's email via the check_login() function
    creator_email = email
    fn = input("""
    What would you like to name your fund?
    """)
    ver = check_fund_name_exists(fn, fund_list)
    if ver == 1:
        print("Your fund is called", fn)
        ed = input("""
        What is the date of the event?
        """)
        print("The date of your event is", ed)
        ev = input("""
        What is the event?
        """)
        print("Your event is", ev)
        gift = input("""
        What is the planned gift?
        """)
        print("The planned gift is ", gift)
        pt = input(
            """What type of participation for your fund: free or fixed?
            """)
        while pt != 'free' and pt != 'fixed':
            print("You must answer the question with fixed or free.")
            pt = input(
                """What type of participation for your fund: free or fixed?
                """
            )
        print("Your fund is ", pt)
        if pt == "fixed":
            amount = input("""
            What amount do you want to fix the fund at?
            """)
        else:
            amount = "free amount"
        print("The fund contribution is ", amount)
        it = input(
            """
            What type of identification for your fund: named or anonymous?
            """)
        while it != 'named' and it != 'anonymous':
            print("You must answer with named or anonymous.")
            it = input(
                """
                What type of identification for your fund: named or anonymous?
                """)
        print("Your fund is ", it)
        emails = get_participants()
        print('The participants\' emails for the fund are ', emails)

        fund["creator_email"] = creator_email
        fund["fund_name"] = fn
        fund["event_date"] = ed
        fund["event_type"] = ev
        fund["gift"] = gift
        fund["participation_type"] = pt
        fund["identification_type"] = it
        fund["participants"] = emails
        fund["amount"] = 0
        fund["comment"] = 0
        # Add the fund dict to the list
        fund_list.append(fund)

def check_fund_name_exists(fn, fund_list):
    # Checks that the fund name doesn't already exist
    for i in range(len(fund_list)):
        v = fund_list[i]["fund_name"]
        if v == fn:
            print("This fund name already exists, please choose another one")
            return 0
    return 1

def get_participants():
    # Returns the list of participants' emails for a fund
    x = input("""
    Enter the number of participants
    """)
    x = verify_int(x)
    participant_list = [] * x
    for i in range(x):
        email_part = input("""
        Enter the email
        """)
        while email_part in participant_list:
            print("This email already exists")
            email_part = input("""
            Enter the email
            """)
        participant_list.append(email_part)
    return participant_list

def add_amount(index, fund_list):
    # Adds participants' amounts to their associated fund
    amount = input("""
    Enter the amount to add to the fund
    """)

    old_amount = fund_list[index]['amount']
    new_amount = (int(old_amount) + (int(amount)))
    # Update the amount in the fund dict
    fund_list[index]['amount'] = new_amount

def participate_in_fund(fund_list):
    # Lets a guest contribute to a fund
    em = 0
    x = 0
    ve = 1
    done = 0
    while done == 0:
        done2 = 0
        em = input("What is your email address?  ")
        while em == "":
            print("please enter a value for the email address  ")
            em = input("What is your email address?  ")
        pas = input("if you forgot your email, type 'forgot' to go back  ")
        if pas == 'forgot':
            done = 1
            done2 = 1
        while done2 == 0:
            for i in range(len(fund_list)):
                ve = fund_list[i]["participants"]
                if em in ve:
                    print(fund_list[i])
                    x = input("""
                    If this is the fund you want to add money to
                    then type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                    x = verify_int(x)
                    while x > 3 or x < 1:
                        print("""Please select a number between 1 and 3 corresponding to your request.""")
                        x = input("""
                        If this is the fund you want to add money to
                        then type 1
                        If you want to move to the next fund type 2
                        To go back type 3
                        """)
                        x = verify_int(x)
                    if x == 1:
                        print("You are connected to the fund ", fund_list[i]["fund_name"])
                        index = i
                        add_amount(index, fund_list)
                        done = 1
                        done2 = 1
                        break
                    if x == 3:
                        done = 1
                        done2 = 1
                        break
            if x != 2:
                done2 = 1

def fund_comments(fund_list, email):
    ve = 1
    done = 0
    while done == 0:
        for i in range(len(fund_list)):
            ve = fund_list[i]["creator_email"]
            if email == ve:
                print(fund_list[i])
                x = input("""
                If this is the fund you want to add a comment to then type 1
                To move to the next fund type 2
                To go back type 3
                """)
                x = verify_int(x)
                while x > 3 or x < 1:
                    print("""Please select a number between 1 and 3 corresponding to your request.""")
                    x = input("""
                    If this is the fund you want to add money to
                    then type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                    x = verify_int(x)
                if x == 1:
                    comment_choice = input("""
                    If you want to add a comment type 1
                    If you want to replace a comment type 2
                    If you want to delete the comment(s) type 3
                    If you want to exit type 4
                    """)
                    while comment_choice != '1' and comment_choice != '2' and comment_choice != '3' and comment_choice != '4':
                        print("error, type 1, 2, 3 or 4")
                        comment_choice = input("""
                    If you want to add a comment type 1
                    If you want to replace a comment type 2
                    If you want to delete the comment(s) type 3
                    If you want to exit type 4
                    """)
                    if comment_choice == "1":
                        # adds the comment to the selected dict
                        com = input("""
                        enter your comment  
                        """)
                        old_comment = fund_list[i]['comment']
                        comment_list = []
                        comment_list.append(com)
                        comment_list.append(old_comment)
                        fund_list[i]['comment'] = comment_list
                        print(email, "added a comment to fund", i + 1)
                    if comment_choice == "2":
                        # replaces the comment in the selected dict
                        com = input("""
                        enter your comment  
                        """)
                        fund_list[i]["comment"] = com
                        print(email, " replaced a comment in fund ", i + 1)
                    if comment_choice == "3":
                        # deletes the comments
                        fund_list[i]["comment"] = 0
                        print(email, "deleted the comment(s) in fund", i + 1)
                    done = 1
                    break
                if x == 3:
                    done = 1

def cancel_fund(cancelled_fund_list, fund_list, email):
    ve = 1
    done = 0
    transferred_fund = 0
    while done == 0:
        for i in range(len(fund_list)):
            ve = fund_list[i]["creator_email"]
            if email == ve:
                print(fund_list[i])
                right_fund = input("""
                    If this is the fund you want to cancel type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                while right_fund != '1' and right_fund != '2' and right_fund != '3':
                    print("error, type 1 or 2")
                    right_fund = input("""
                    If this is the fund you want to cancel type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                if right_fund == '1':
                    transferred_fund = fund_list[i]
                    fund_list[i]["amount"] = 0
                    # Add the corresponding fund dict to cancelled_fund_list
                    cancelled_fund_list.append(transferred_fund)
                    fund_list.pop(i)
                    print("Fund", i + 1, "is cancelled")
                    done = 1
                    break
                if right_fund == '3':
                    done = 1
                    break

def delete_fund(fund_list, email):
    ve = 1
    done = 0
    while done == 0:
        for i in range(len(fund_list)):
            ve = fund_list[i]["creator_email"]
            if email == ve:
                print(fund_list[i])
                right_fund = input("""
                    If this is the fund you want to delete type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                while right_fund != '1' and right_fund != '2' and right_fund != '3':
                    print("error, type 1 or 2")
                    right_fund = input("""
                    If this is the fund you want to delete type 1
                    If you want to move to the next fund type 2
                    To go back type 3
                    """)
                if right_fund == '1':
                    # resets the amount, which corresponds to the fund's money
                    fund_list[i]["amount"] = 0
                    done = 1
                    print("fund", i + 1, "is deleted")
                    break
                if right_fund == '3':
                    done = 1
                    break

def profile_comments(user_list, email):
    ve = 1
    done = 0
    while done == 0:
        for i in range(len(user_list)):
            ve = user_list[i]["email"]
            if email == ve:
                print("comment: ", user_list[i]["comment"])
                comment_choice = input("""
                If you want to add a comment type 1
                If you want to replace a comment type 2
                If you want to delete the comment(s) type 3
                If you want to exit type 4
                """)
                while comment_choice != '1' and comment_choice != '2' and comment_choice != '3' and comment_choice != '4':
                    print("error, type 1, 2, 3 or 4")
                    comment_choice = input("""
                If you want to add a comment type 1
                If you want to replace a comment type 2
                If you want to delete the comment(s) type 3
                If you want to exit type 4
                """)
                if comment_choice == "1":
                    # adds the comment to the selected dict
                    com = input("""
                    enter your comment  
                    """)
                    old_comment = user_list[i]['comment']
                    comment_list = []
                    comment_list.append(com)
                    comment_list.append(old_comment)
                    user_list[i]['comment'] = comment_list
                    print(email, " added a comment to their profile")
                if comment_choice == "2":
                    # replaces the comment in the selected dict
                    com = input("""
                    enter your comment  
                    """)
                    user_list[i]["comment"] = com
                    print(email, " replaced their comment")
                if comment_choice == "3":
                    # deletes the comments
                    user_list[i]["comment"] = 0
                    print(email, "deleted their comment")
                done = 1
                break


# MAIN PROGRAM
menu = 0
menu2 = 0
data = 0
fund_file = 0
cancelled_fund_file = 0
user_list = []
fund_list = []
cancelled_fund_list = []

data = open("data.json", "a")
if (os.path.getsize("data.json") == 0):
    json.dump(user_list, data)
data.close()

with open("data.json", "r") as f:
    # loads the list from the file
    user_list = json.load(f)

# opens the funds file and initializes a list for it
fund_file = open("funds.json", "a")
# checks the file size and creates an empty list if the file is empty
if (os.path.getsize("funds.json") == 0):
    json.dump(fund_list, fund_file)
fund_file.close()
with open("funds.json", "r") as f:
    # loads the list from the file
    fund_list = json.load(f)

cancelled_fund_file = open("cancelled_funds.json", "a")
if (os.path.getsize("cancelled_funds.json") == 0):
    json.dump(cancelled_fund_list, cancelled_fund_file)
cancelled_fund_file.close()
with open("cancelled_funds.json", "r") as f:
    # loads the list from the file
    cancelled_fund_list = json.load(f)

while menu != 4:
    menu = main_menu()
    if menu == 1:
        registration(user_list)
    if menu == 2:
        email = check_login(user_list)
        exit_submenu = 0
        while exit_submenu == 0:
            menu2 = fund_menu()
            if menu2 == 1:
                create_fund(user_list, fund_list, email)
            if menu2 == 2:
                print("You are in the fund comments area.")
                fund_comments(fund_list, email)
            if menu2 == 3:
                print("You are in the cancel a fund area.")
                cancel_fund(cancelled_fund_list, fund_list, email)
            if menu2 == 4:
                print("You are in the delete a fund area.")
                delete_fund(fund_list, email)
            if menu2 == 5:
                print("You are in your profile comment area.")
                profile_comments(user_list, email)
            if menu2 == 6:
                exit_submenu = 1
                print("returning to main menu")
    if menu == 3:
        print("Contributing to a fund")
        participate_in_fund(fund_list)
    if menu == 4:
        print("You have exited the site.")

        with open("data.json", "w") as f:
            # writes the updated list to the json file
            json.dump(user_list, f, indent=3, separators=(',', ': '))

        with open("funds.json", "w") as f:
            # writes the updated list to the json file
            json.dump(fund_list, f, indent=3, separators=(',', ': '))

        with open("cancelled_funds.json", "w") as f:
            # writes the updated list to the json file
            json.dump(cancelled_fund_list, f, indent=3, separators=(',', ': '))