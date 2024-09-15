import json



from hi_and_bye import  *
from create_task import create_task
from search_list_tasks import *
from update_delete_task import *

PATH_TO_JSON = "all_tasks.json"

""" call_actions function acts as main menu from which the user can select different options"""

def call_actions(selected_option:str):
    if selected_option == "1":
        create_task(PATH_TO_JSON)
    elif selected_option == "2":
        choose_update_or_delete(PATH_TO_JSON)
    elif selected_option == "3":
        search_list_all(PATH_TO_JSON)
    elif selected_option == "4":
        print(say_goodbye())
        return False
    return True


