""" save changes helps our user not to make mistake when choosing to delete or update"""


def save_changes() -> bool:
    user_answer = input("To save the changes type 'yes', otherwise type 'no': ")
    if user_answer == "yes":
        print(f"You have selected {user_answer}.")
        return True
    elif user_answer == "no":
        print(f"You have selected {user_answer}.")
        return False
    else:
        print(f"{user_answer} is not a valid option!")
        save_changes()


def loading():
    pass
"""I could not figure out what loading is supposed to do."""