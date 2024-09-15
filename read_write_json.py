import json
from call_action import *

""" write json - the name speaks for itself"""


def write_json(output_file, my_task):
    with open(output_file, 'w') as file_to_write:
        json.dump(my_task, file_to_write, indent=4)


""" read json - the name speaks for itself. I thought its a nice way to show function with parameter with default value. This way we can use read json to both display the full list of tasks 
or print out a filtered version of it. Now that I am looking at it, probably it has few too many if statements """


def read_json(input_file, text_to_filter=None) -> dict:
    if text_to_filter:
        try:
            with open(input_file, "r") as file_to_read:
                data = json.load(file_to_read)
                if is_json_empty(data):
                    filtered_dict = {key: value for key,value in data.items() if text_to_filter in data[key]["task_name"]}
                    if filtered_dict:
                        return filtered_dict
                    else:
                        print(f"No tasks have {text_to_filter} in their task name.")
        except json.decoder.JSONDecodeError:
            print("The JSON file is empty.")
    else:
        with open(input_file, "r") as file_to_read:
            try:
                data = json.load(file_to_read)
                return data
            except json.decoder.JSONDecodeError:
                data = {}
                return data


"""dict reader helps us to better visualize the content of a dictionary"""


def dict_reader(some_dict: dict):
    if some_dict:
        for k, v in some_dict.items():
            print(f"This task has a task id of {k} and its details are {v}.")
    else:
        pass



""" is json empty allows us to check if a json file is empty or not. this is useful to prevent few bugs in read json functions"""


def is_json_empty(some_dict) -> bool:
    if len(some_dict) == 0:
        print("The json file is empty.")
        return False
    return True
