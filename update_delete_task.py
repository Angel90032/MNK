from read_write_json import read_json, write_json
from search_list_tasks import *
from common import *

"""choose update or delete does exactly what one might suggest"""


def choose_update_or_delete(json_task):
    user_choice = input("Write 'exit' to return to previous menu, "
                        "write 'update' to update an existing task or "
                        "write 'delete' to delete an existing task: ")

    if user_choice == "exit":
        print("You chose to exit rather than delete or update a task.")
    elif user_choice == "delete":
        delete(json_task)
    elif user_choice == "update":
        update(json_task)
    else:
        print(f"{user_choice} is not a valid option")
        choose_update_or_delete()


"""delete - self explanatory. part of the main functions of our program"""


def delete(json_task):
    search_list_all(json_task)
    valid_key = key_validator(read_json(json_task))
    print(f"The valid key is {valid_key}")
    data = read_json(json_task)
    popped_item = data.pop(valid_key)

    if save_changes():
        write_json(json_task, data)
        print(f"You have successfully removed task {popped_item}.")


def update(json_task):
    search_list_all(json_task)
    valid_key = key_validator(read_json(json_task))
    print(f"The valid task id is {valid_key}")
    data = read_json(json_task)
    data[valid_key]["task_name"] = update_property(valid_key, data, "task_name")
    data[valid_key]["task_description"] = update_property(valid_key, data, "task_description")
    data[valid_key]["task_status"] = update_property(valid_key, data, "task_status")
    if save_changes():
        write_json(json_task, data)


""" key validator makes sure that the selected key is present in the dictionary. 
downside to it is that I have not given an option to break out of the loop without providing a valid key"""


def key_validator(some_dict: dict):
    user_key_selection = input("Select a task id: ")
    if user_key_selection in some_dict.keys():
        return user_key_selection
    else:
        print(f"{user_key_selection} is not a valid task id!")
        while True:
            user_input = input("Write 'exit' to return to previous menu or 'continue' to remain in current menu.")
            if user_input == "exit":
                print("Returning to previous menu")
                break
            elif user_input == "continue":
                key_validator(some_dict)
            else:
                continue


"""update property helps us to update the task name, description or status, depending on a 3rg parameter my property.
 I am somewhat proud of figuring out this solution, I have a feeling it might be correct"""

def update_property(validated_key, some_data, my_property):
    user_input = ""
    if my_property == "task_name":
        user_input = input("Enter new name of the task, press ENTER to keep the current one: ")
    elif my_property == "task_description":
        user_input = input("Enter new description of the task, press ENTER to keep the current one: ")
    elif my_property == "task_status":
        print("Enter new status of the task: ")
        user_input = is_status_valid()

    if len(user_input) == 0:
        return some_data[validated_key][my_property]
    else:
        return user_input


"""is status valid helps us to accept only valid statuses when updating a task"""


def is_status_valid():
    some_status = input("Enter 'pending' or 'completed' status for the task, press ENTER to keep the current one: ")
    if some_status == "pending" or some_status == "completed" or some_status == '':
        return some_status
    else:
        print(f"Your selection {some_status} has to be either pending or completed!")
        is_status_valid()


