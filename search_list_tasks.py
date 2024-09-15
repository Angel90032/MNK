import json
from read_write_json import *
from read_write_json import read_json

""" search list all functions helps us to display all of the tasks or filter the output based on a substring in the name. 
I have a feeling that some of the functionality that I wrote in read json belongs here... in terms of keeping actions organized in a more logical way"""


def search_list_all(file):
    user_search_option = input("Enter a substring to display all tasks which contain this substring in their name.\n"
                               "If you want to display all current tasks write 'list': ")
    if user_search_option == "list":
        try:
            dict_reader(read_json(file))
        except json.decoder.JSONDecodeError:
            print("File is empty, no tasks to display!")
    else:
        dict_reader(read_json(file, user_search_option))
