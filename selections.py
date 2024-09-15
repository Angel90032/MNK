""" This file contains the codes and text for Task Management System version 1.00 and the related selection functions"""

CREATE_TASK_CODE = "1"
CREATE_TASK_TEXT = "Create a new task"
UPDATE_DELETE_TASK_CODE = "2"
UPDATE_DELETE_TASK_TEXT = "Update or delete an existing task"
SEARCH_TASK_CODE = "3"
SEARCH_TASK_TEXT = "Search for task"
EXIT_PROGRAM_CODE = "4"
EXIT_PROGRAM_TEXT = "Exit the program"

"""Once a valid selection is made by the user, 
the successful selection message function will display some reply in order to make the program more user friendly"""

def successful_selection_message(verified_user_selection_code:str):
    if verified_user_selection_code == "1":
        return f"You have selected {CREATE_TASK_CODE} in order to {CREATE_TASK_TEXT}."
    elif verified_user_selection_code == "2":
        return f"You have selected {UPDATE_DELETE_TASK_CODE} in order to {UPDATE_DELETE_TASK_TEXT}."
    elif verified_user_selection_code == "3":
        return f"You have selected {SEARCH_TASK_CODE} in order to {SEARCH_TASK_TEXT}."
    elif verified_user_selection_code == "4":
        return f"You have selected {EXIT_PROGRAM_CODE} in order to {EXIT_PROGRAM_TEXT}!"


""" purpose of the selection_is_valid function is to check if the user selected a valid option"""


def selection_is_valid(selection:str) -> str:
    valid_options = [CREATE_TASK_CODE, UPDATE_DELETE_TASK_CODE, SEARCH_TASK_CODE, EXIT_PROGRAM_CODE]
    if selection in valid_options:
        return selection
    print(f"Your selection {selection} is invalid!")
    select_option()


""" select_options displays some useful info to the user and accepts his input if its valid"""


def select_option() -> str:
    print(f"Select one of the following options:\n"
          f" {CREATE_TASK_CODE} to {CREATE_TASK_TEXT}\n"
          f" {UPDATE_DELETE_TASK_CODE} to {UPDATE_DELETE_TASK_TEXT}\n"
          f" {SEARCH_TASK_CODE} to {SEARCH_TASK_TEXT}\n"
          f" {EXIT_PROGRAM_CODE} to {EXIT_PROGRAM_TEXT}")

    user_selection = input("What would you like to choose: ")
    verified_user_selection = selection_is_valid(user_selection)
    print(successful_selection_message(verified_user_selection))
    return verified_user_selection