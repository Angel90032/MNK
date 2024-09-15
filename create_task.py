""""""
from read_write_json import read_json, write_json

'''the find max key function does exactly what it suggests, it find key with the highest number if a certain dictionary and returns it'''
def find_max_key(some_dict:dict):
    keys = [int(key) for key,value in some_dict.items()]
    if len(keys) != 0:
        max_key = max(keys)
    else:
        max_key = 0
    return max_key


""" task number generator yields the current max key and increments it by 1 to return the next free task number """
def task_number_generator(number):
    n = number + 1
    while True:
        yield n

"""create task functions help us to create a new task, by default at first the status is pending"""

def create_task(json_task):
    mydict = read_json(json_task)
    all_numbers = task_number_generator(find_max_key(mydict))
    task_number = str(next(all_numbers))
    task_name = input("Enter the name of your task: ")
    task_description = input("Enter the description of your task: ")
    task_status = "pending"
    mydict[task_number] = {
        "task_number": task_number,
        "task_name": task_name,
        "task_description": task_description,
        "task_status": task_status
    }

    #write_json("all_tasks.json", mydict)
    write_json(json_task, mydict)
    print(f"You have successfully create a new task with task number {task_number}, "
          f"description {task_description}, "
          f"status {task_status}")




