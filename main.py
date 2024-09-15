''' this is function which allows the user to select an option to either create a task, update/delete a task or search all tasks or specific tasks'''

from selections import *
from call_action import *


if __name__ == "__main__":
    print(say_hello())

    while call_actions(select_option()):
        call_actions(select_option())












